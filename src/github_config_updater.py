import json

def update_github_config(
    repo,
    branch,
    incident
):

    file_path = incident["configFile"]

    github_file = repo.get_contents(
        file_path,
        ref=branch
    )

    config = json.loads(
        github_file.decoded_content.decode()
    )

    audit_changes = []

    for change in incident["changes"]:

        parameter = change["parameter"]

        new_value = change["newValue"]

        old_value = config.get(parameter)

        config[parameter] = new_value

        audit_changes.append(
            f"{parameter}: {old_value} -> {new_value}"
        )

    updated_content = json.dumps(
        config,
        indent=4
    )

    repo.update_file(
        path=file_path,
        message=f"{incident['incidentId']} Auto Remediation",
        content=updated_content,
        sha=github_file.sha,
        branch=branch
    )

    return config, audit_changes