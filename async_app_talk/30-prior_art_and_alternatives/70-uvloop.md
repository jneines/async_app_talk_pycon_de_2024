# uvloop

> uvloop is a fast, drop-in replacement of the built-in asyncio event loop. uvloop is implemented in Cython and uses libuv under the hood.
>
> by MagicStack, Inc.

[Documentation](https://uvloop.readthedocs.io)
[Github](https://github.com/MagicStack/uvloop)

:::{code} python

import asyncio
import sys

import uvloop

async def main():
    # Main entry-point.
    ...

if sys.version_info >= (3, 11):
    with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
        runner.run(main())
else:
    uvloop.install()
    asyncio.run(main())

:::
[Back](00-introduction.md)
