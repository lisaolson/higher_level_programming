#!/bin/bash
# Takes in a URL as an argument, sends GET request to URL, displays body
curl -sL -X GET $1 -H "X-HolbertonSchool-User-Id: 98"
