from github_helper import get_repo

def create_branch(branch_name):

    repo = get_repo()

    main_branch = repo.get_branch("main")

    print(f"Creating branch: {branch_name}")

    repo.create_git_ref(
        ref=f"refs/heads/{branch_name}",
        sha=main_branch.commit.sha
    )

    return repo