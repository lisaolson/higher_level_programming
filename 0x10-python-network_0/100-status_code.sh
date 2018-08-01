#!/bin/bash
# Takes in a URL as an argument, sends GET request to URL, displays body
curl $1 -sI -w "%{http_code}" -o /dev/null
