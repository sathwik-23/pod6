from github_helper import get_repo

def create_branch(branch_name):

    repo = get_repo()

    main = repo.get_branch("main")

    repo.create_git_ref(
        ref=f"refs/heads/{branch_name}",
        sha=main.commit.sha
    )

    return repo