import subprocess
from dotenv import dotenv_values
from github import Github


def main():
    print(vars(dotenv_values(".env")))


if __name__ == "__main__":
    main()
