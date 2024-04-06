# Trio

> A friendly Python library for async concurrency and I/O
>
> mainly by: Nathaniel J. Smith

[Documentation](https://trio.readthedocs.io/en/stable/)
[Github](https://github.com/python-trio/trio)

:::{code} python

# tasks-intro.py

import trio


async def child1():
    print("  child1: started! sleeping now...")
    await trio.sleep(1)
    print("  child1: exiting!")


async def child2():
    print("  child2: started! sleeping now...")
    await trio.sleep(1)
    print("  child2: exiting!")


async def parent():
    print("parent: started!")
    async with trio.open_nursery() as nursery:
        print("parent: spawning child1...")
        nursery.start_soon(child1)

        print("parent: spawning child2...")
        nursery.start_soon(child2)

        print("parent: waiting for children to finish...")
        # -- we exit the nursery block here --
    print("parent: all done!")


trio.run(parent)

:::
[Back](00-introduction.md)
