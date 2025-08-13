import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()
repo_name = "test_repo"
branch_name = "update-readme"
owner = "jiasidhugill"
"""Open a pull request via GitHub API."""
url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls"
headers = {
    "Authorization": f"Bearer {os.getenv("GITHUB_TOKEN_FINEGRAINED")}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}
data = {
    "title": "title",
    "head": branch_name,
    "base": "main",
    "body": "body"
}
response = requests.post(url, json=data, headers=headers).json()
print(response)
# print(json.dumps(response, indent=4))