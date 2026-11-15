
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Data model
class Feedback(BaseModel):
    name: str
    message: str


# Home API
@app.get("/")
def home():
    return {"message": "Backend is running!"}


# Feedback API
@app.post("/feedback")
def submit_feedback(data: Feedback):

    return {
        "success": True,
        "message": "Feedback submitted successfully!",
        "name": data.name,
        "feedback": data.message
    }
