
from pydantic import BaseModel

class GithubRepoResponse(BaseModel):
    name: str
    html_url: str
    readme: str 