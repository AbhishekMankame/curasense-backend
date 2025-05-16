from fastapi import FastAPI
from app.routes import predict # Import the router module

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello, welcome to CuraSense"}

app.include_router(predict.router)
