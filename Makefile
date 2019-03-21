env:
	pipenv shell

.PHONY : test
test:
	python -m unittest tests/test_prob1.py