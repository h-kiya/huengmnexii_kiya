from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)


@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "status": 200,
    }
