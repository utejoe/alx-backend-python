#!/usr/bin/env python3

import asyncio
from random import uniform

'''
This module defines an asynchronous coroutine called wait_random,
which takes an integer argument (max_delay, default value of 10),
and returns a random delay between 0 and max_delay (inclusive).
'''

async def wait_random(max_delay: int = 10) -> float:
    '''Generates a random number and returns it after n delay'''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
