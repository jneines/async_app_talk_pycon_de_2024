book:
	jupyter-book build async_app_talk

open:
	open async_app_talk/_build/html/index.html

clean:
	rm -rf async_app_talk/_build

all: clean book
