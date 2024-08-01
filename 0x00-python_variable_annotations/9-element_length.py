#!/usr/bin/env python3
""" Annotations of iterables """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function that takes in an iterable object and returns a
        list of tuples where contains an element from the
        iterable object and it's length.
    """
    return [(i, len(i)) for i in lst]
