#!/usr/bin/python3
"""
This defines a class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle using Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Intialize attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def attribute_validator(var, value):
        """ Validates and handles all error messages """

        width_height = ["width", "height"]
        xy = ["x", "y"]

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var))
        if var in width_height and value <= 0:
            raise ValueError("{} must be > 0".format(var))
        if var in xy and value < 0:
            raise ValueError("{} must be >= 0".format(var))

    @property
    def width(self):
        """
        The getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter for width
        Args:
            value (int): the width to set
        """
        self.attribute_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
        The getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter for height
        Args:
            value (int): the height to set
        """
        self.attribute_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
        The getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ The setter for x
        Args:
            value (int): the value to assign to x
        """

        self.attribute_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
        The getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        the setter for y
        Args:
            value (int): the value to assign to y
        """
        self.attribute_validator("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return (self.width * self.height)

    def display(self):
        """
        Returns string representation of Rectangle
        """
        print("\n"*self.y, end="")
        for _ in range(self.height):
            print(" "*self.x + "#"*self.width)

    def __str__(self):
        """
        Returns the representation of Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y,
                    self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates attributes of the Rectangle
        Args:
            args (non-keyword arguments): non-specified amount of arguments
            kwargs (key-word arguments): non-specified amount of arguments
        """

        attrs = ["id", "width", "height", "x", "y"]

        for pos, val in enumerate(args):
            if pos < len(attrs):
                setattr(self, attrs[pos], val)

        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the instance
        """

        new_dict = {}
        attrs = ["id", "width", "height", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict
