#!/usr/bin/python3
"""sends a POST request to the passed URL with an email"""
import sys
import requests


if __name__ == "__main__":
    val = {"email": sys.argv[2]}
    print(requests.post(sys.argv[1], data=val).text)
