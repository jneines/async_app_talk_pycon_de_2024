# Putting it all together


The `AsyncApp` implementation offers a very simple interface.

- It can execute tasks only
- Tasks are defined using `task_descriptions`
- It can be configured using config_files, environment variables and command line arguments

A `task_description` is a simple `dict` with a few known keywords.

The first keyword is `kind`. Valid values are `init`, `continuous`, `periodical` and `cleanup`.

- All `init` tasks are executed right after the applications startup.
- `continuous` and `periodical` tasks are executed until the application or task stops.
- `cleanup` tasks are promised to be run at applications exit.

All `task_descriptions` require a `function` parameter to be set, which defines the action to be called.

There are optional `*args` and `**kwargs` arguments to configure the callback `functions`.

The `periodicals` require a setting to define periodicity. Either `call_every` or a `frequency` setting can be used for that.

