# So, what's asyncio? A brief introduction.


Asyncio has been introduced as a possible solution mainly for I/O related performance problems.

The traditional way to handle I/O often ends up in code, which blocks the execution of concurrent elements in an application, often resulting in bad performance.

The usual suspects when dealing with these problems, such as multiprocessing and threading, are often considered to be complex and not straightforward in use, especially for beginners.
I believe that proper threading and multiprocessing, with all its interprocess or shared memory communication, locks and race condition prevention, as well as efficient object handling still requires a deep understanding of the architecture and inner workings, and is still mainly a topic for experts.

Asyncio comes to the rescue here offering a layer of abstraction at a lower and much easier to understand layer.
While it is no solution to aid in distributing code execution to gain more performance, it will solve the blocking issues quite effiently.



## Interested in a deep dive into asyncio?

Search no further! Just go here:

[Python Asyncio: The complete guide](https://superfastpython.com/python-asyncio/) by Jason Brownlee.
