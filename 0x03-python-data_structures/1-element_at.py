#!/usr/bin/python3
def element_at(my_list, idx):
    if not my_list:
        return

    if idx < len(my_list):
        return my_list[idx]
    elif idx >= len(my_list):
        return None
    else:
        return None
