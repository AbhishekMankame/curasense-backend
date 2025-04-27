from fastapi import FastAPI
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

# Now you can access like
# secret_key = os.getenv("SECRET_KEY")
# print(secret_key)

# Initialize the FASTAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to CuraSense!"}