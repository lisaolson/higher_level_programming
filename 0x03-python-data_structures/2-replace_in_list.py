#!/usr/bin/python3
if __name__ == "__main__":
    def replace_in_list(my_list, idx, element):
        if idx > 0 and idx <= len(my_list):
            my_list[idx] = element
            return my_list
        elif idx > len(my_list):
            return None
        else:
            return None
