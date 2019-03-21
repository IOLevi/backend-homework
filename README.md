# lola-backend

MAKE A VIRTUAL ENV SO THAT IT WILL NOT HAVE A PROBLEM ON THEIR SERVER

https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv

If pip/pip3 is already installed:
`sudo pip3 install --user pipenv`

Crude installation (if pip is not already installed). Run the following command.
`curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python`

MAKE INSTRUCTIONS ON HOW TO WORK IT

pipenv installation instructions:

cd lola
sudo pipenv install

--pipenv install

--pipenv shell
    opens a shell with access to all installed dependencies. Can run program as "python <filename>"
--pipenv run pip
    runs with dependencies. E.g., "python <filename>"


Find out what’s changed upstream: $ pipenv update --outdated.
Upgrade packages, two options:
Want to upgrade everything? Just do $ pipenv update.
Want to upgrade packages one-at-a-time? $ pipenv update <pkg> for each outdated package.

only need to remove the colon so that the iso offset is only 5 chars instead of 6

CAN USE MAKEFILE TO MAKE A GENERIC SCRIPT TO INSTALL DEPENDENCIES AND THEN RUN TESTS

KNOWN ISSUES:
Assumes linearly sorted fares and legs array by fare_id. Binary search will fail if list is not complete and sorted.