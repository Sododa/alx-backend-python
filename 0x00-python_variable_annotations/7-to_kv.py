#!/usr/bin/env python3
'''task 7'''
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return float of v'''
    return (k, float(v**2))
