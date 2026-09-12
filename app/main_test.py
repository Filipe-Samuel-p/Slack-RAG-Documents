from integrations.github.client import get_github_client

gh = get_github_client()

repos = gh.get_repos()

for repo in repos:
    print(f"Repository: {repo.name}, URL: {repo.html_url}")
    

