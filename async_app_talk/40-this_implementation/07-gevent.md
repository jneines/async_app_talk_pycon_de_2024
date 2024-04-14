# Gevent

> gevent is a coroutine -based Python networking library that uses greenlet to provide a high-level synchronous API on top of the libev or libuv event loop.
>
> by Denis Bilenko

[Homepage](http://www.gevent.org)
[Documentation](http://www.gevent.org)
[Github](https://github.com/gevent/gevent.git)

:::{code} python

import gevent
from gevent import socket

urls = ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

_ = gevent.joinall(jobs, timeout=2)

[job.value for job in jobs]

['74.125.79.106', '208.77.188.166', '82.94.164.162']

:::

[Back](01-this_was_before_and_thats_related.md)
