#!/bin/bash
# Takes in a URL, sends request to that URL, displays size of body
curl -s -I $1 | grep "Content-Length" | cut -d " " -f 2
