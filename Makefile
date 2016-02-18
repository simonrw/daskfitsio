help:
	@echo "Tasks: test coverage"

test:
	py.test

coverage:
	py.test --cov daskfitsio.py --cov-report html
