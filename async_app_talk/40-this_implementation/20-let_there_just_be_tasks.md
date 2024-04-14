# Let there just be tasks

Another requirement is to have all implementations to run things based on tasks.

And these tasks will be executed concurrently.
For this to be possible we require the following:

- Each task must be interruptible or cancelable
- Periodic calls are done in a while loop with dynamic sleeps to match the call frequency
- Event listeners respect timeouts to allow interrupting work and will be executed in a while loop as well
- The while loops condition is a singleton `keep_running` variable which is imported from a module, used by all tasks and can be changed by any task at any time to end all tasks execution.
