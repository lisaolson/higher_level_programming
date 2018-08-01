#!/bin/bash
# Takes in a URL as an argument, sends GET request to URL, displays body
curl -sI -w "%{http_code}" $1 -o /dev/null
