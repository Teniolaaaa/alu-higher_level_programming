#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request with custom header, and displays the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"

