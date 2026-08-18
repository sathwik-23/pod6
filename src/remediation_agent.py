from .incident_reader import load_incident
from .config_updater import update_config
from .github_branch import create_branch
from .github_commit import upload_file
from .github_pr import create_pr

class RemediationAgent:

    def execute(self):

        incident = load_incident(
            "incidents/INC1001.json"
        )

        updated_config, changes = update_config(
            incident["configFile"],
            incident["changes"]
        )

        branch_name = (
            incident["incidentId"] + "-auto-fix"
        )

        repo = create_branch(branch_name)

        upload_file(
            repo=repo,
            branch=branch_name,
            local_file="configs/appsettings.json",
            remote_file="configs/appsettings.json"
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