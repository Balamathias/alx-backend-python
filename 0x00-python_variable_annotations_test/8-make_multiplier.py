#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
    '''
    def multiply(n: float) -> float:
        return (n * multiplier)
    return multiply
