#!/usr/bin/env python3
"""This python function takes two integer
arguments page and page_size.

It returns a tuple of size two containing a
start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination
parameters.

The first page is page 1.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters.
    """
    return ((page-1) * page_size, page_size * page)
