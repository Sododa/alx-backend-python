#!/usr/bin/env python3
"""task 1"""
from importlib import import_module as using
from typing import List


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""
    random_nums = [num async for num in async_generator()]
    return random_nums
