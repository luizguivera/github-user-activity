import requests

def github_activity(username):
    url = f'https://api.github.com/users/{username}/events/public'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
events = github_activity('luizguivera')

for event in events:
    print(f"Event Type: {event['type']}, Repo: {event['repo']['name']}, Created At: {event['created_at']}")
