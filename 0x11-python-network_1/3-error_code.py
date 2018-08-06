#!/usr/bin/python3
# Takes in a URL, sends a request, displays X-Request-Id value

import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            utf8 = html.decode('utf-8')
        print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.reason))
