#!/usr/bin/env python3
"""task 102"""
from typing import Union
from typing import Mapping
from typing import Any
from typing import TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """type var"""
    if key in dct:
        return dct[key]
    else:
        return default
