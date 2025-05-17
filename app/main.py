from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis
from decouple import config

from app.db.postgres import get_db
from app.db.redis import get_redis
from app.core.logger import logger  # <-- логгер
from app.routers import users


app = FastAPI()
app.include_router(users.router)
# CORS
origins = config("CORS_ORIGINS", default="http://localhost:8080").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    client_ip = request.client.host
    method = request.method
    path = request.url.path

    logger.info(f"📥 {method} {path} from {client_ip}")

    try:
        response = await call_next(request)
    except Exception as exc:
        logger.exception(f"❌ Error while handling {method} {path} from {client_ip}: {exc}")
        raise

    logger.info(f"📤 {method} {path} -> {response.status_code}")
    return response


# Log on app startup
logger.info("🚀 FastAPI application is starting...")

# Endpoints
@app.get("/users/")
async def get_users(session: AsyncSession = Depends(get_db)):
    logger.info("GET /users/ called")
    return {"message": "Postgres connected successfully!"}


@app.get("/cache/")
async def get_cache(redis_conn: redis.Redis = Depends(get_redis)):
    logger.info("GET /cache/ called")
    value = await redis_conn.get("key")
    return {"key": value or "no value yet"}


@app.get("/")
async def health_check():
    logger.info("GET / (health_check) called")
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }


# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


if __name__ == "__main__":
    import uvicorn

    HOST = config("HOST")
    PORT = int(config("PORT"))

    logger.info(f"Starting Uvicorn server at {HOST}:{PORT}")
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
