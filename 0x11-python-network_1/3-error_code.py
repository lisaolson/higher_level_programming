#!/usr/bin/python3
# Takes in a URL, sends a request, displays X-Request-Id value

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
