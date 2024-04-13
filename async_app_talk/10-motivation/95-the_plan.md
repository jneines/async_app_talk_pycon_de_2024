# The plan

... So a plan was born

- streamline implementations
- find a suitable base all apps can have in common
- integrate monitoring and configuration concepts
- split functionality into several apps following the traditional unix philosophy
- let them communicate via redis
- use systemd targets to run the apps
- use an asyncio based implementation for concurrency

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.
>
> -- Malcom Douglas McIlroy - Inventor of the Unix pipes

Do not end with a cite?
