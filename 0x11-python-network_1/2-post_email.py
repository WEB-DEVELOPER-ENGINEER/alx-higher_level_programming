#!/usr/bin/python3
"""sends a POST request to the passed URL with an email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    req = urllib.request.Request(url, urllib.parse.urlencode(data).encode())
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
