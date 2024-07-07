#!/usr/bin/env python3

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Function that takes a lst of any type and returns its first element.
    '''
    if lst:
        return lst[0]
    else:
        return None
