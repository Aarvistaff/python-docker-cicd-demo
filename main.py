
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Docker Deployment Demo V2",
        "status": "updated automatically",
        "deployment": "GitHub to Render using Docker"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
