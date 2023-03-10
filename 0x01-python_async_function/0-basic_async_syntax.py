#!/usr/bin/env python3
""" defines a aynchronous coroutine that takes an integer argument and
returns the maxdelay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """function to evaluate a sleep time, await it and return the time"""
    sec = random.uniform(0, max_delay)
    await asyncio.sleep(sec)
    return sec
