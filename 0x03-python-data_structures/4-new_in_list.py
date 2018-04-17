#!/usr/bin/python3
if __name__ == "__main__":
    def new_in_list(my_list, idx, element):
        new_list = my_list[:]

        if idx > 0 and idx <= len(new_list):
            new_list[idx] = element
            return new_list
        elif idx > len(my_list):
            return None
        else:
            return None
