#!/usr/bin/env python3
"""task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Write an asynchronous coroutine"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
