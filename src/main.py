import datetime
import sys

from github import Github


def main():
    github_access_token = sys.argv[1]
    github = Github(github_access_token)
    repo_name = "JosephTLyons/action_minutes_test"
    repository = github.get_repo(repo_name)

    issue_to_edit = repository.get_issue(number=1)
    current_datetime = datetime.datetime.now()
    issue_to_edit.edit(body=f"Hi {current_datetime}")


if __name__ == "__main__":
    main()
