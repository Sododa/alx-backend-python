#!/usr/bin/env python3
'''task 9'''
from typing import Iterable
from typing import List
from typing import Sequence
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''retun i and len'''
    return [(i, len(i)) for i in lst]
