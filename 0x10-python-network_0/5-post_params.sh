#!/bin/bash
# Takes in a URL, sends POST request to passed URL, displays body
curl -sL $1 -X POST -d "email=hr@closchool.com&subject=I will always be here for PLD"
