from datetime import datetime

from incident_reader import load_incident

from github_branch import create_branch

from github_config_updater import (
    update_github_config
)

from github_pr import create_pr


class RemediationAgent:

    def execute(self):

        incident = load_incident(
            "incidents/INC1001.json"
        )

        branch_name = (
            incident["incidentId"]
            + "-"
            + datetime.now().strftime(
                "%Y%m%d%H%M%S"
            )
        )

        repo = create_branch(
            branch_name
        )

        updated_config, changes = (
            update_github_config(
                repo,
                branch_name,
                incident
            )
        )

        pr_url = create_pr(
            repo,
            branch_name,
            incident["incidentId"]
        )

        return (
            incident,
            updated_config,
            changes,
            pr_url
        )