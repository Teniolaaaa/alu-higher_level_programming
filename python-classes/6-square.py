#!/usr/bin/python3
"""
6-square module
Defines a Square class with size, position properties and printing method.
"""


class Square:
    """Square class with size, position, and print functionality."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve position value."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position value with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # considering position."""
        if self.__size == 0:
            print()
            return
        # Print vertical offset
        for _ in range(self.__position[1]):
            print()
        # Print each line with horizontal offset + size #
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

