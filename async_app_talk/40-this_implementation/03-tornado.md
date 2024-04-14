# Tornado

> Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

[Homepage](https://www.tornadoweb.org/en/stable/)
[Documentation](https://www.tornadoweb.org/en/stable/)
[Github](https://github.com/tornadoweb/tornado)

:::{code} python

import asyncio
import tornado

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

:::

[Back](01-this_was_before_and_thats_related.md)
