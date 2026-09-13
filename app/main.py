from fastapi import FastAPI
from app.api.github_routers import router as github_router

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "ok"}

app.include_router(github_router)