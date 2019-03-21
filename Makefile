# Install pipenv, install dependencies
install:
	sudo pip3 install --user pipenv
	pipenv install

# Run unittests
.PHONY : test
test:
	pipenv run python -m unittest tests/test_prob1.py
	pipenv run python -m unittest tests/test_prob2.py

# Run prob1 and prob2 with sample inputs
.PHONY : sample
sample:
	pipenv run python prob1.py sample
	pipenv run python prob2.py sample

# POST prob1 and prob2 to the server
.PHONY : deploy
deploy:
	pipenv run python prob1.py
	pipenv run python prob2.py