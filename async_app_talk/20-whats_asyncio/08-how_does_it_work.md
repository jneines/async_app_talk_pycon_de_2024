# How does it work?

What actually needs to be done in order to run several tasks in parallel without using threads is to make them interceptable, so that Python can execute parts of every task one after another and with that emulate parallel execution. This strategy is fine for many tasks.

- Tasks waiting for some input to arrive
- high level handling of I/O

It wont work for CPU intensive tasks. Here real parallelism is the only answer.

So how does it work? 

Basically we need to tell the interpreter, that a function execution needs to be treated differently, that there are places in the code, where execution can be interrupted. That's where the `async` keyword is for.

All actions that can be interrupted are marked with the `await` keyword. At every occurence of `await` the execution can be interruped to switch the context.

Here are two functions from the Python standard library:
    
    `time.sleep` vs `asyncio.sleep`

The result of both is exactly the same. Ones nature is blocking though, whilst the other allows interception to execute something else.

And finally you need a `runner` to execute the `async awaitables`. That's where `asyncio.run` comes into play.


