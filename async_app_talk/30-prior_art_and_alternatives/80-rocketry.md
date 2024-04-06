# Rocketry

> Rocketry is a modern statement-based scheduling framework for Python. It is simple, clean and extensive. It is suitable for small and big projects.
>
> by Mikael Koli

[Documentation](https://rocketry.readthedocs.io)
[Github](https://github.com/Miksus/rocketry)

:::{code} python

from rocketry import Rocketry
from rocketry.conds import daily

app = Rocketry()

@app.task(daily)
def do_things():
    ...

if __name__ == "__main__":
    app.run()


:::
[Back](00-introduction.md)
