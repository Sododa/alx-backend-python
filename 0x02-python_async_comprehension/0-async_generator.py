#!/usr/bin/env python3
"""task 0"""
import asyncio
import random


async def async_generator():
    """Write a coroutine called async_generator that takes no arguments."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
