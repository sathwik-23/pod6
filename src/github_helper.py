from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

def get_repo():

    token = os.getenv("GITHUB_TOKEN")

    github = Github(token)

    repo = github.get_repo(
        os.getenv("REPO_NAME")
    )

    return repo