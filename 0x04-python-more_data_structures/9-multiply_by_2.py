#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, v in a_dictionary.items():
        d = {k: (v * 2)}
        a_dictionary.update(d)
    return (a_dictionary)
