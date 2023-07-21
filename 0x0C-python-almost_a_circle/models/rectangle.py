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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
