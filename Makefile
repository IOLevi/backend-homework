# Enter into the virtual environment
env:
	pipenv shell

# Run unittests
.PHONY : test
test:
	python -m unittest tests/test_prob1.py
	python -m unittest tests/test_prob2.py

# Run prob1 and prob2 with sample inputs
.PHONY : sample
sample:
	python prob1.py sample
	python prob2.py sample

# POST prob1 and prob2 to the server
.PHONY : deploy
deploy:
	python prob1.py
	python prob2.py