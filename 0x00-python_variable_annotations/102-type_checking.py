#!/usr/bin/env python3

"""
Type Checking

This module defines a function zoom_array that takes a tuple and an optional integer factor as arguments. It returns a tuple by zooming in on the elements of the input list.

"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zoom Array

    This function takes a tuple and an optional integer factor as arguments and returns a tuple by zooming in on the elements of the input list.

    Args:
        lst: A tuple of elements.
        factor: An optional integer factor (default is 2).

    Returns:
        A tuple with zoomed-in elements.

    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array: List[int] = [12, 72, 91]

zoom_2x: Tuple = zoom_array(array)

zoom_3x: Tuple = zoom_array(array, 3)
