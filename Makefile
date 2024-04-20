target:=async_app_talk
all: book

new: clean book

book:
	jupyter-book build $(target)

open:
	open $(target)/_build/html/index.html

clean:
	rm -rf $(target)/_build
