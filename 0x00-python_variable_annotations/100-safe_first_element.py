#!/usr/bin/env python3
from typing import Any, Union

def safe_first_element(lst: list) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None