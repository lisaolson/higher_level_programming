#!/usr/bin/python3

import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)
print(my_list)

i = 0
while (sys.argv != '\0'):
    print(sys.argv)
    i += 1
