import sys
import requests

def get_latest_events(username):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)

    if response.status_code == 200:
        latest_events = response.json()
        print(latest_events)

        for event in latest_events:
                if event['type'] == 'IssueCommentEvent':
                    print(f"Commented on issue {event['payload']['issue']['number']}")
                elif event['type'] == 'PushEvent':
                    print(f"Pushed to {event['repo']['name']}")
                elif event['type'] == 'IssuesEvent':
                    print(f"Created issue {event['payload']['issue']['number']}")
                elif event['type'] == 'WatchEvent':
                    print(f"Starred {event['repo']['name']}")
                elif event['type'] == 'PullRequestEvent':
                    print(f"Created pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'PullRequestReviewEvent':
                    print(f"Reviewed pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'PullRequestReviewCommentEvent':
                    print(f"Commented on pull request {event['payload']['pull_request']['number']}")
                elif event['type'] == 'CreateEvent':
                    print(f"Created {event['payload']['ref_type']} {event['payload']['ref']}")
                else:
                    print(f"{event['type']}")
    else:
        print(f"Error fetching events for {username}: {response.status_code}") 

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_events(sys.argv[1])
    else:
        print("Please provide a GitHub username as a command line argument.")