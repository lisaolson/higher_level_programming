#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for x in new_list:
        return [x % 2 == 0 for x in new_list]
        # if my_list[x] % 2 == 0:
          #  new_list.append(True)
        #else:
         #   new_list.append(False)
    # return (new_list)
# return [ x % 2 == 0 for x in new_list]
