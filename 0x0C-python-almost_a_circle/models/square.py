#!/usr/bin/python3
"""
This defines a class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the print() and str() representation of this square."""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """return size of this square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates attributes of the Square"""

        D_attributes = ["id", "size", "x", "y"]

        for position, val in enumerate(args):
            if pos < len(D_attributes):
                setattr(self, D_attributes[position], val)

        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square
        """

        D_dictionary = {}
        attributes = ["id", "size", "x", "y"]

        for i in attributes:
            D_dictionary[i] = getattr(self, i)

        return D_dictionary
