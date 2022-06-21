import sys

from dotenv import dotenv_values
from github import Github


def main():
    print(str(sys.argv))
    print(vars(dotenv_values(".env")))


if __name__ == "__main__":
    main()
