from remediation_agent import RemediationAgent
import json

agent = RemediationAgent()

incident, config, changes, pr_url = agent.execute()

print("\n====================")
print("INCIDENT PROCESSED")
print("====================")

print(f"\nIncident ID: {incident['incidentId']}")

print("\nChanges Applied:")

for change in changes:
    print(change)

print("\nUpdated Config:")

print(
    json.dumps(
        config,
        indent=4
    )
)

print("\nPull Request:")

print(pr_url)