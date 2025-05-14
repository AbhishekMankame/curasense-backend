from fastapi import FastAPI
from dotenv import load_dotenv
from app import predict # Import the whole predict module

# Load environment variables
load_dotenv()

# Initialize the FASTAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to CuraSense!"}

# Include the predict router
app.include_router(predict.router)