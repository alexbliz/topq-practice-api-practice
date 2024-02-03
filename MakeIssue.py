import requests
import json

class GitHubAPI:
    def __init__(self, repository_owner, repository_name, token):
        self.repository_owner = repository_owner
        self.repository_name = repository_name
        self.token = token

    def create_github_issue(self):
        url = f'https://api.github.com/repos/{self.repository_owner}/{self.repository_name}/issues'
        headers = {'Authorization': f'token {self.token}'}

        issue_data = {
            'title': "Alex's issue",
            'body': "This issue was created via REST API from Python by Alex Bliznichenko",
            'assignees': ['topq-practice'],
            'labels': ['practice1']
        }

        r = requests.post(url, json.dumps(issue_data), headers=headers)
        if r.status_code == 201:
            print('Successfully created the issue.')
            new_issue_number = r.json()['number']
            print(f'New issue number: {new_issue_number}')
        else:
            print('Could not create the issue.')
            print('Response:', r.content)

    def get_open_issues_count(self):
        url = f'https://api.github.com/repos/{self.repository_owner}/{self.repository_name}/issues'
        headers = {'Authorization': f'token {self.token}'}

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            issues = r.json()
            print(f'Number of open issues: {len(issues)}')
        else:
            print(f'Could not retrieve issues')
            print('Response:', r.content)

    def get_issues_with_label(self, label):
        url = f'https://api.github.com/repos/{self.repository_owner}/{self.repository_name}/issues?labels={label}'
        headers = {'Authorization': f'token {self.token}'}

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            issues = r.json()
            print(f'Number of issues with label "{label}": {len(issues)}')
        else:
            print(f'Could not retrieve issues with label "{label}"')
            print('Response:', r.content)



repository_owner = "topq-practice"
repository_name = "api-practice"
token = "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"

github_api = GitHubAPI(repository_owner=repository_owner, repository_name=repository_name, token=token)
github_api.create_github_issue()
github_api.get_open_issues_count()
github_api.get_issues_with_label('practice1')
