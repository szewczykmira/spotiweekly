lint:
	@black .

run:
	@flask run


install:
	@poetry install

test:
	@pytest


.DEFAULT_GOAL = run
