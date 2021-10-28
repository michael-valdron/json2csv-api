# 2021-10-28
# As of the time of writing PIPENV run scripts function is broken, using make tasks as a replacement

FLASK_APP=json2csv_api
CMD=FLASK_APP=$(FLASK_APP) flask

runserver:
	$(CMD) run

tests:
	pytest -v

repl:
	python

.phony: runserver test repl