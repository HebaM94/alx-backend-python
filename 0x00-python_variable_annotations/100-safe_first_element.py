#!/usr/bin/env python3
""" Annotations of duck-typing """
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first element of iterable if not empty else None """
    if lst:
        return lst[0]
    else:
        return None
