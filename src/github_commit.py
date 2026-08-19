def upload_file(
        repo,
        branch,
        local_file,
        remote_file):

    contents = repo.get_contents(
        remote_file,
        ref=branch
    )

    with open(local_file, "r") as file:
        content = file.read()

    repo.update_file(
        path=contents.path,
        message="Auto Remediation",
        content=content,
        sha=contents.sha,
        branch=branch
    )