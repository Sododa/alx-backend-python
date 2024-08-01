#!/usr/bin/env python3
from typing import Iterable
from typing import List
from typing import Sequence
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
