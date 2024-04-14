# AnyIO

> AnyIO is an asynchronous networking and concurrency library that works on top of either asyncio or trio. It implements trio-like structured concurrency (SC) on top of asyncio and works in harmony with the native SC of trio itself.
>
> Applications and libraries written against AnyIO’s API will run unmodified on either asyncio or trio. AnyIO can also be adopted into a library or application incrementally – bit by bit, no full refactoring necessary. It will blend in with the native libraries of your chosen backend.
>
> by Alex Grönholm

[Documentation](https://anyio.readthedocs.io/en/stable/)
[Github](https://github.com/agronholm/anyio)

:::{code} python

import sniffio
import trio
from anyio import sleep


async def main():
    print('Hello')
    await sleep(1)
    print("I'm running on", sniffio.current_async_library())

trio.run(main)

:::

[Back](01-this_was_before_and_thats_related.md)
