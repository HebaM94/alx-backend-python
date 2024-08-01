#!/usr/bin/env python3
""" Annotated multipler used by another function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return multiplier multiplied by floats """
    def multiply(num: float) -> float:
        """ Callback to multiply num with multiplier """
        return num * multiplier

    return multiply
