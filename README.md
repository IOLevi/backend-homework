# Lola Backend Homework
API/Backend challenge project to evaluate coding style. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Installation assumes pip3 is installed on the target system. If pip3 is not installed, run the following command:

Linux/Debian:
```
sudo apt install python3-pip
```

MacOS:
```
brew install python3
```

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
* [pipenv](https://pipenv.readthedocs.io/en/latest/) - Python Dev Workflow for Humans
* [requests](http://docs.python-requests.org/en/master/user/quickstart/) - Python Requests library


## Versioning

I use [GitHub](http://github.com/iolevi) for versioning. This project is hosted in a private repo.

## Known Issues:
Project assumes fares and legs array in JSON payload are in ascending order, and binary search is used to optimize speed. Binary search will fail if data is unsorted or indexes are missing. 

## Author

* **Evan Sznol**