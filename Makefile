# Enter into the virtual environment
env:
	pipenv shell

# Run unittests
.PHONY : test
test:
	python -m unittest tests/test_prob1.py
	python -m unittest tests/test_prob2.py