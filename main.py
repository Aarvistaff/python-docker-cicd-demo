
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Docker Deployment Demo V1",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
