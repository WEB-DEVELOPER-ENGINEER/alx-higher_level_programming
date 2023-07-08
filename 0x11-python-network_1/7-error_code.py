#!/usr/bin/python3
"""Sends a request to a given URL"""
import sys
import requests


if __name__ == "__main__":
    if requests.get(sys.argv[1]).status_code >= 400:
        print("Error code: {}".format(requests.get(url).status_code))
    else:
        print(requests.get(url).text)
