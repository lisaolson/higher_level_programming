#!/usr/bin/python3

import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    list_args = load_from_json_file("add_item.json")
except Exception:
    list_args = []

for i in sys.argv[1:]:
    list_args.append(i)

save_to_json_file(list_args, "add_item.json")
