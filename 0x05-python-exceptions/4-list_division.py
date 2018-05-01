#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    total = 0

    for x in range(list_length):
        try:
            total = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            total = 0
        except TypeError:
            print("wrong type")
            total = 0
        except IndexError:
            print("out of range")
            total = 0
        finally:
            new_list.append(total)
    return new_list
