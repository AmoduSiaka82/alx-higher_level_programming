#!/usr/bin/python3
def number_keys(a_dictionary):
    new_list = []
    for k, v in a_dictionary.items():
        new_list.append(k)
    return len(new_list)
