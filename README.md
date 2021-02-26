# Hypothesis Ledger Exercices

This python package is composed of 2 scripts

- A CLI application for displaying the balance of a given account name `ledger.py`
- A sample data generator `sampler.py` to generate transactions history to test the CLI application



## Requirements

- python >=3.7
- pip
- virtualenv

## Install

``` 
virtualenv .venv --python=/usr/bin/python3
source .venv/bin/activate
pip install -r requirements.txt
```


## Run

```bash
#generate the random sample
(.venv)me@computer$ python sampler.py > sample.csv
# get the balance for john
(.venv)me@computer$ cat sample.csv | python ledger.py john
# get the balance for john on the 1st of January 2020
(.venv)me@computer$ cat sample.csv | python ledger.py john --date=2020-01-01
# get the balance for john with another file
(.venv)me@computer$ cat sample.csv | python ledger.py john --date=2020-01-01

```
## Tests
```bash
(.venv)me@computer$ pytest -vv 
```
 

## Developer Notes

### Input

* As no input method was specified we choose to provide 2 options
- input file as an option in cli `<-i>`
- handle the use of pipe to redirect stdin to app


### Output

* As no output format was specified we choose for the demonstration
to first display in the full transactions history for the given account name
and then the balance with date and account name 

* The main function that calculates balance return the result in float and can be reused


### Generate sample

We choose to output to stdout the result and not writing the results into a static file
to ease tests and checks and because of a lack of specification on the tests that will be done

We could pipe the sampler with the main app and proceed to extensive tests 
```
python sampler.py | python ledger.py john 2015-03-03
```

