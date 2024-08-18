from fastapi import FastAPI
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from .routes import router as student_router
from .db import db  # Importing to ensure MongoDB connection

app = FastAPI()

# MongoDB Connection
MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client["your_database_name"]

# Include the router from routes.py
app.include_router(student_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI + MongoDB!"}