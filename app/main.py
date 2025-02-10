from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

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