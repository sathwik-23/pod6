def create_pr(
        repo,
        branch_name,
        incident_id
):

    pr = repo.create_pull(
        title=f"{incident_id} Auto Remediation",
        body=f"""
Incident ID: {incident_id}

This PR was generated
by the Incident Remediation Agent.
""",
        head=branch_name,
        base="main"
    )

    return pr.html_url