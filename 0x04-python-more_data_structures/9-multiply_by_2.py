#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    new_dic.update(a_dictionary)
    for k, v in new_dic.items():
        d = {k: (v * 2)}
        new_dic.update(d)
    return (new_dic)
