#!/usr/bin/python3
""" class of empty rectangle that defines a rectangle"""



class Rectangle:
    """ class rectangle"""
    def _init_(self, width=0, height=0)
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width
        """
        return self._width
    @property
    def height(self):
        """ height
        """
        return self._height

    @width.setter
    def width(self, value):
        """ width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        """
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    
