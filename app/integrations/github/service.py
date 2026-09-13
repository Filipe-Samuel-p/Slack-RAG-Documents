
from app.integrations.github.client import get_github_client
from app.api.schemas.github import GithubRepoResponse
from github import GithubException

def get_github_repos() -> list[GithubRepoResponse]:

 gh = get_github_client()

 repos = gh.get_user().get_repos()

 repo_list = []
 for repo in repos:
    try:
       repo_readme = repo.get_readme().decoded_content.decode("utf-8")
    except GithubException:
       repo_readme = "NO README"

    repo_list.append(GithubRepoResponse(
      name=repo.full_name,
      html_url=repo.html_url,
      readme=repo_readme
    ))

    gh.close()
 return repo_list
