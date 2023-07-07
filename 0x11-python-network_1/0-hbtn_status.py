#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.read())))
        print("\t- content: {}".format((response.read())))
        print("\t- utf8 content: {}".format(response.read().decode("utf-8")))
