# Threads

A **thread** based application will perform many things at the same time using **many threads** in a **single process**

- due to the GIL things might not happen at the same time although expected otherwise
- performance gain may be small if workload is compute intense
- noticable acceleration for independent I/O related tasks though
- communication between threads can be tricky
- synchronizing threads is tricky
- loss of control can lead to threads no longer being managable


