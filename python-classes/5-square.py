#!/usr/bin/python3
"""
5-square module
Defines a Square class with my_print method to print the square.
"""


class Square:
    """Square class with size property and printing method."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        self.size = size

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

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)

