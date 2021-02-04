bandit:
	@bandit .

lint:
	@black . && flake8

run:
	@flask run


install:
	@poetry install && npm install


update:
	@poetry update && npm update

test:
	@pytest


.DEFAULT_GOAL = run
