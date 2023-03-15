#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    t = len(my_list)
    if idx < 0 or idx >= t or t == 0:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
