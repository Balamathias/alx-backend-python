#!/usr/bin/env python3

from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar, None] = None) -> Union[Any, TypeVar]:
    '''
    Function that takes a dictionary dct, a key key and an optional default value.
    Returns the value linked to key in dct if it exists, otherwise default.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
