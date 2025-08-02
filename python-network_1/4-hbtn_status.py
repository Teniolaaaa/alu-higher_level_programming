#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using requests and prints response details."""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
