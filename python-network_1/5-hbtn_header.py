#!/usr/bin/python3
"""Takes a URL, sends a request, and displays X-Request-Id from the response header using requests."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
