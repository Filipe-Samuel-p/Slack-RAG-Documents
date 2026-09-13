from fastapi import APIRouter
from app.integrations.github.service import get_github_repos as gtr

router = APIRouter()

@router.get("/github/repos")
async def get_github_repos():
    return gtr()