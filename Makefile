lint:
	@black .

run:
	@flask run


install:
	@poetry install


.DEFAULT_GOAL = run
