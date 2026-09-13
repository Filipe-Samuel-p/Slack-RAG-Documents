from github import Github, Auth 
from app.config import get_settings
from typing import Iterator



def get_github_client() -> Iterator[Github]:
    token = get_settings().github_token

    if not token:
        raise ValueError("GitHub token is not set in the environment variables")

    auth = Auth.Token(token=token)

    return Github(
        auth=auth
    )

