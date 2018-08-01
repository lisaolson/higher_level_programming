#!/bin/bash
# Returns status code
curl -s -w "%{http_code}" -I $1 -o /dev/null
