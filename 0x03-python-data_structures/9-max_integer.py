#!/usr/bin/python3
def max_integer(my_list=[]):
    x =len(my_list)
    if len(my_list) == 0:
        return "None"
    else:
        my_list.sort()
        return my_list[x - 1]
