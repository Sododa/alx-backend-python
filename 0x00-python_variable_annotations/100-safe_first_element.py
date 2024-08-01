#!/usr/bin/env python3
"""task 100"""
from typing import Sequence
from typing import Union
from typing import Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe first element"""
    if lst:
        return lst[0]
    else:
        return None
