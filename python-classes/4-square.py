#!/usr/bin/python3
"""
4-square module
Defines a Square class with size property getter and setter.
"""


class Square:
    """Square class with private size and property accessors."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        self.size = size  # Use property setter for validation

    @property
    def size(self):
        """Retrieve size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size value with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

