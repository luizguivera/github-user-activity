import requests

def github_activity(username):
    url = f'https://api.github.com/users/{username}/events/public'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
events = github_activity('luizguivera')

def format_event(event):
    repo = event["repo"]["name"]
    type = event["type"]

    if type == "PushEvent":
        commits = len(event["payload"]["commits"])
        return f"Pushed {commits} commits to {repo}"

    if type == "WatchEvent":
        return f"Starred {repo}"

    if type == "CreateEvent":
        return f"Created something in {repo}"

    return f"{type} in {repo}"

for event in events:
    print(format_event(event))
