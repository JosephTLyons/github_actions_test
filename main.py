import subprocess
from dotenv import dotenv_values
from github import Github


def main():
    github_access_token = dotenv_values(".env")["GITHUB_ACCESS_TOKEN"]
    print(github_access_token)


if __name__ == "__main__":
    main()
