from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)

app.state.message = "Hello World"


@app.get("/message")
async def get_message():
    return {
        "message": app.state.message,
        "status": 200,
    }


@app.post("/message")
async def post_message(message):
    app.state.message = message
    return {
        "message": app.state.message,
        "status": 200,
    }
