from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from app.db.postgres import get_db
from app.db.redis import get_redis
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis

app = FastAPI()

origins = config("CORS_ORIGINS", default="http://localhost:8080").split(",")

HOST = config("HOST")
PORT = int(config("PORT"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Пример эндпоинта, использующего Postgres
@app.get("/users/")
async def get_users(session: AsyncSession = Depends(get_db)):
    # Пример запроса (будет работать при наличии модели User)
    # result = await session.execute(select(User))
    # return result.scalars().all()
    return {"message": "Postgres connected successfully!"}

# ✅ Пример эндпоинта, использующего Redis
@app.get("/cache/")
async def get_cache(redis_conn: redis.Redis = Depends(get_redis)):
    # await redis_conn.set("key", "value")
    value = await redis_conn.get("key")
    return {"key": value or "no value yet"}

@app.get("/")
async def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)