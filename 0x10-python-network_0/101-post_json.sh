#!/bin/bash
# Sends POST request w/ filename as arg
curl -sL $1 -X POST -H "Content-Type: application/json" -d @$2
