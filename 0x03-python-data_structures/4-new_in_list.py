#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
    return my_list
copy_list = my_list[:]
copy_list[idx] = element
return copy_list
