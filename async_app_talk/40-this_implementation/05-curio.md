# Curio

> Curio is a coroutine-based library for concurrent Python systems programming using async/await. It provides standard programming abstractions such as tasks, sockets, files, locks, and queues as well as some advanced features such as support for structured concurrency. It works on Unix and Windows and has zero dependencies. You'll find it to be familiar, small, fast, and fun.
>
> by Dave Beazley

[Documentation](https://curio.readthedocs.io/en/latest/)
[Github](https://github.com/dabeaz/curio)

:::{code} python

# hello.py
import curio

async def countdown(n):
    while n > 0:
        print('T-minus', n)
        await curio.sleep(1)
        n -= 1

async def kid(x, y):
    print('Getting around to doing my homework')
    await curio.sleep(1000)
    return x * y

async def parent():
    kid_task = await curio.spawn(kid, 37, 42)
    count_task = await curio.spawn(countdown, 10)

    await count_task.join()

    print("Are you done yet?")
    result = await kid_task.join()

    print("Result:", result)

if __name__ == '__main__':
    curio.run(parent)

:::
[Back](01-this_was_before_and_thats_related.md)
