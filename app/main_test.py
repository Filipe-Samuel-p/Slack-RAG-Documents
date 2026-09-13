
from app.integrations.github.client import get_github_client
from app.api.schemas.github import GithubRepoResponse
from github import GithubException

def get_github_repos() -> list[GithubRepoResponse]:

 gh = get_github_client()

 repos = gh.get_user().get_repos()

 result = []
 for repo in repos:

    try:
        repo_readme = repo.get_readme().decoded_content.decode("utf-8")
    except GithubException:
       readme = "NO README"



    result.append(GithubRepoResponse(
      name=repo.full_name,
      html_url=repo.html_url,
      readme=repo_readme
    ))

    print(f"repo_name: {repo.full_name}")
 return result


get_github_repos()