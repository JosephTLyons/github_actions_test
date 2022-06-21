import sys

from dotenv import dotenv_values
from github import Github


def main():
    github = Github(sys.argv[1])


if __name__ == "__main__":
    main()
