#!/usr/bin/python3
"""takes your GitHub credentials and uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    for commit in req.json()[:10]:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print("{}: {}".format(sha, author))
