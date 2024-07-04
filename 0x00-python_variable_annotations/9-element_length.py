#!/usr/bin/env python3

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    '''
    Function that takes a list lst of strings as argument and returns a list of tuples.
    Each tuple contains a string and an int representing the length of the string.
    '''
    return [(i, len(i)) for i in lst]
