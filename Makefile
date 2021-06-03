bandit:
	@bandit .

lint:
	@black . && flake8

run:
	@flask run


install:
	@poetry install


update:
	@poetry update

test:
	@pytest


.DEFAULT_GOAL = run
