#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: the list of waiting times the wait_n function executed
    """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes wait_random n times"""
    waitings = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(waitings)
