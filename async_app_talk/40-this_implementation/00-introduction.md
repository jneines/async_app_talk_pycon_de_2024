# The AsyncApp Framework

> Simple things should be simple, complex things should be possible
>
> -- Alan Kay

Over the years I did quite some implementations for applications that, when looking back, have been quite comparable. So at some point, I wanted to streamline the approach as maintaining all these different code bases became harder and harder.

Although all applications served different purposes, it became obvious that all could be done if a framework offered these features:

For application **execution**:

- Run functionality concurrently
- there may be long running jobs, some may be called periodically, or on certain events

Regarding execution **tracing**:

- be configurably verbose
- allow some monitoring functionality

And regarding **configuration**:

- respect suitable default settings
- configure settings via a configuration file
- change them via command line parameters ...
- ... or via environment variables

