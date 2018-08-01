#!/bin/bash
# Takes in a URL as an argument, sends GET request to URL, displays body
curl -sL -w "%{http_code}" -I $1 -o /dev/null
