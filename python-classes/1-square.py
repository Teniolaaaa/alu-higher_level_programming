#!/usr/bin/python3
"""
1-square module
Defines a Square class with private size attribute.
"""


class Square:
    """Square class with private size attribute."""

    def __init__(self, size):
        """Initialize square with size (no validation)."""
        self.__size = size

