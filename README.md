# Lola Backend Homework
API/Backend challenge project to evaluate coding style. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Installation assumes pip3 is installed on the target system. If pip3 is not installed, run the following command:

Ubuntu/Debian:
```
sudo apt install python3-pip
```

MacOS:
```
brew install python3
```

2. Installation uses pyenv to manage python versions, allowing pipenv to automatically install the specified Python version (3.6). To install, run the following commands:

MacOS:
```
brew install pyenv
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
$ exec "$SHELL"
```

Ubuntu (bash):
```
cd
git clone git://github.com/yyuu/pyenv.git .pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
cd -
```

For additional installation options, see the [pyenv](https://github.com/pyenv/pyenv#installation) installation guide. 
### Installing

Installation is bootstrapped with with the make utility, which will install pipenv (if not present) on --user, and automatically install the required dependencies into the pipenv environment. Simply run the following command:
```
make install
```

## Running the tests

Tests are automated with the make utility. Run tests with the following command:
```
make test
```

## Deployment
Deployment (POSTing each problem solution) to the server is automated with the make utility. Sample data can be posted with the following command:
```
make sample
```

Problems 1 and 2 (not sample) can be run with the following command:
```
make deploy
```

## Built With

* [Make](https://www.gnu.org/software/make/) - Make utility
* [pyenv](https://github.com/pyenv/pyenv) - Python versioning system
* [pipenv](https://pipenv.readthedocs.io/en/latest/) - Python Dev Workflow for Humans
* [requests](http://docs.python-requests.org/en/master/user/quickstart/) - Python Requests library


## Versioning

I use [GitHub](http://github.com/iolevi) for versioning. This project is hosted in a private repo.

## Known Issues:
Project assumes fares and legs array in JSON payload are in ascending order, and binary search is used to optimize speed. Binary search will fail if data is unsorted or indexes are missing. 

## Author

* **Evan Sznol**