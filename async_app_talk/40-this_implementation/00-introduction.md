# The AsyncApp Framework

> Simple things should be simple, complex things should be possible
>
> -- Alan Kay

Over the years I did quite some implementations for applications that, when looking back, have been quite comparable. So at some point, I wanted to streamline the approach as maintaining all these different code bases became harder and harder.

Although all applications served different purposes, it became obvious that all of them could be based on the same foundation, if a framework offered the following features.

For application **execution**:

- Run functionality concurrently
- allow long running jobs, periodically executing ones and those listening for events at the same time

Regarding execution **tracing**:

- be configurably verbose
- allow some monitoring functionality to track system resources

And regarding **configuration**:

- respect suitable default settings
- allow configuration via a configuration file
- and change it via command line parameters ...
- ... or via environment variables

