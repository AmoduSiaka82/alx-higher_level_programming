#!/usr/bin/python3
"""

It composed by a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: text must be a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for k in ".?:":
        list_text = s.split(k)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + k if s is "" else s + "\n\n" + i + k

    print(s[:-3], end="")
