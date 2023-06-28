import requests
import json

# Define the repository and event details
repository = 'facundofacio/repository_dispatch_test'
event_type = 'custom_event_type'
with open("config.json") as json_file:
    PERSONAL_ACCESS_TOKEN = json.load(json_file).get("token")
# Create the payload for the repository_dispatch event
payload = {
    'event_type': event_type,
    'client_payload': {
        'param1': 'Hello',
        'param2': 'World!'
    }
}

# Make a POST request to trigger the GitHub Action workflow
response = requests.post(
    url=f'https://api.github.com/repos/{repository}/dispatches',
    headers={
        "Accept": "application/vnd.github.v3+json",
        'Authorization': f'Bearer {PERSONAL_ACCESS_TOKEN}',
        "Content-Type": "application/json",
        },
    json=payload
    )

# Check the response status code
if response.status_code == 204:
    print(f"Workflow triggered successfully for event: {event_type}")
else:
    print(
        f"Failed to trigger workflow. Response status code: {response.status_code}")
    print(response.text)
