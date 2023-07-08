#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter"""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}
    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
