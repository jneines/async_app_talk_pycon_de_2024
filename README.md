# AsyncApp. My contribution to hype Pythons asyncio a bit more

Asyncio use is now everywhere in the Python world, ...

.. or is it?

Being there since version 3.4 my impression is, that it is still not the go to solution when starting off new projects.
It's not an obvious choice and traditional approaches still seem to be much preferred especially by beginners.

So let me take you with me on a journey to create simple, yet powerful building blocks to build asyncio based applications using patterns that are easy to follow, lightweight and attractive.

## Usage

### Building the book

If you'd like to develop and/or build the AsyncApp. My contribution to hype Pythons asyncio a bit more book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `async_app_talk/` directory
4. Run `jupyter-book clean async_app_talk/` to remove any existing builds
5. Run `jupyter-book build async_app_talk/`

A fully-rendered HTML version of the book will be built in `async_app_talk/_build/html/`.

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/jneines/async_app_talk/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
