#!/usr/bin/env python3
""" Annotated sttring, int or flaot module """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float] ) -> Tuple[str, float]:
    """ Return a tuple of string and float """
    return (k, (v * v))
