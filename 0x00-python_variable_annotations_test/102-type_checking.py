#!/usr/bin/env python3

from typing import List, Union


def zoom_array(lst: List[Union[int, float]], factor: float = 2.0) -> List[Union[int, float]]:
    '''
    Function that takes a list lst of integers and floats and returns a new list.
    The new list should contain all elements from lst multiplied by factor.
    The list should be the same length as lst. The new list should have the same type as lst.
    '''
    return ([i * factor for i in lst])
