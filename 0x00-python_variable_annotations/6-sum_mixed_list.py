#!/usr/bin/env python3
""" Annotated list of mixed values module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of the list of inregers and floats """
    return sum(mxd_lst)
