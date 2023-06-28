import json
import requests


def trigger_github_action(owner, repo, workflow_file, ref):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_file}/dispatches"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer <YOUR_PERSONAL_ACCESS_TOKEN>"
    }
    payload = {
        "ref": ref
    }
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 204:
        print("GitHub Action triggered successfully.")
    else:
        print(
            f"Failed to trigger GitHub Action. Status code: {response.status_code}.")
        print(response.text)


# Set the repository information and workflow file name
owner = "facundofacio"
repo = "repository_dispatch_test"
workflow_file = ".github/workflows/triggered_workflow.yml"
ref = "main"  # e.g., "main" or "refs/heads/main"

# Call the function to trigger the GitHub Action
trigger_github_action(owner, repo, workflow_file, ref)
