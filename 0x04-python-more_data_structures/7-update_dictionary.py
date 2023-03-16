#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if k == key:
            d = {k: value}
            a_dictionary.update(d)
        else:
            d = {key: value}
            a_dictionary.update(d)
    return (a_dictionary)
