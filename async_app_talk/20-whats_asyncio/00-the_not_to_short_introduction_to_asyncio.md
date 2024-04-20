# The not to short introduction to asyncio

- **Asyncio** is one of the three implementations for parallel and **concurrent processing** in Pythons standard library
- Can execute many things in a **single thread** and **single process**
- Workload has to be mainly
    -  I/O related
    -  envolve a lot of waiting
    -  interruptible
 
- whereas multiprocessing and threading can deal with classic Python code ...
- ... Asyncio needs a suitable implementation of all core functionality that's **ready to be interruptible**

- whereas multiprocessing and threading need a central element for managing execution (e.g. `ThreadPool`, `ProcessPool`) ...
- ... Asyncio manages executes everything in a **main loop**.
