#!/usr/bin/python3
"""Displays the X-Request-Id header variable"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    print(requests.get(url).headers.get("X-Request-Id"))
