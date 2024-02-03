import requests
import json
from MakeIssue import GitHubAPI

repository_owner = "topq-practice"
repository_name = "api-practice"
TOKEN = "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"


github_api = GitHubAPI(repository_owner=repository_owner, repository_name=repository_name, token=TOKEN)
github_api.create_github_issue()
github_api.get_open_issues_count()
github_api.get_issues_with_label('practice1')
github_api.execute_workflow()
