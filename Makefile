bandit:
	@bandit .

lint:
	@black . && flake8

run:
	@flask run


install:
	@poetry install

test:
	@pytest


.DEFAULT_GOAL = run
