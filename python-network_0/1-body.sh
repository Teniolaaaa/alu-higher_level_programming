#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response only for status code 200
curl -s -L "$1"

