from github import Github, Auth 
from config import settings

settings = settings.get_settings()

def get_github_client() -> Github:
    token = settings.github_token
    if not token:
        raise ValueError("GitHub token is not set in the environment variables.")
    auth = Auth.Token(token)

    gh = Github(auth=auth, base_url=settings.github_url)

    return gh

