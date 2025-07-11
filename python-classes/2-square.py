#!/usr/bin/python3
"""
2-square module
Defines a Square class with size validation.
"""


class Square:
    """Square class with private size attribute and validation."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

