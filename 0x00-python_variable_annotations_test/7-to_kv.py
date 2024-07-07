#!/usr/bin/env python3

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''
    Function that takes a string k and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k. The second element is the square of the int OR float v.
    '''
    return (k, v * v)
