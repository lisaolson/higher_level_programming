#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'r+') as f:
        text = json.dumps(my_obj, f)
        f.write(text)
