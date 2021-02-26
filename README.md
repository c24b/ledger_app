# Hypothesis Ledger Exercices

This python package is composed of 2 scripts

- A CLI application for displaying the balance of a given account name `ledger.py`
- A sample data generator `sampler.py` to generate transactions history and test the CLI application


## Requirements

### System requirements
- python >=3.7
- pip
- virtualenv

### Python requirements

- docopt
- pytest
see [requirements.txt](requirements.txt)

## Install

```bash
$ virtualenv .venv --python=/usr/bin/python3
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
```


## Run

1. Generate a random transaction history 

```bash
# generate the random sample
(.venv)me@computer$ python sampler.py > sample.csv
# generate more transactions 100 *3
# Note the total transaction number are multiplied by 3 as their is 3 types of transactions
# account name exchange, expenses, revenues
(.venv)me@computer$ python sampler.py -l 100 > sample300.csv
```
2. Get the balance for one account name

given a file:
```bash
# get the balance for john using pipe
(.venv)me@computer$ cat sample300.csv | python ledger.py john
# get the balance for john using pipe on the 1st of January 2020
(.venv)me@computer$ cat sample300.csv | python ledger.py john --date=2020-01-01
# get the balance for john using option 
(.venv)me@computer$ python ledger.py john --date=2020-01-01 -i example.csv
```

given a string input

```bash
# get the balance for john using pipe
(.venv)me@computer$ echo '2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00' | python ledger.py john
# get the balance for john using pipe on the 1st of January 2020
(.venv)me@computer$ echo '2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00' | python ledger.py john --date=2020-01-01
```


> All in one:
```bash
# generate the sample and then check the balance
(.venv)me@computer$ python sampler.py | python ledger.py claire --date=2020-01-01
```


## Tests

Execute the test for the CLI application

```bash
(.venv)me@computer$ pytest -vv 
```

## Getting help

- ledger.py usage: `ledger.py -h`

- sampler.py usage: `sampler.py -h`


## Documentation

see [docs](./docs/)

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

Output example:
```
=== TRANSACTIONS: john ===
2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00

=== BALANCE: john ===
day	account name	balance (§)
2015-01-17	john	-145.00 §
```

### Generate sample

We choose to output to stdout the result and not writing the results into a static file
using python 
to ease tests and checks and because of a lack of specification on input format.

We could pipe the sampler with the main app and proceed to extensive tests 

```
python sampler.py | python ledger.py john 2015-03-03
```

We could also test that the application has correct results comparing expected results with 
the actual results

```python
from .ledger import get_balance
from .ledger import import_data
from .ledger import build_history

#input as a str
input_test = '''...
'''
#input_file
with open(myfile.csv, 'r') as f:
    input_test = f.read()
 
expected_results = [(name, balance, None), (name, balance, date), ...]


input_history = build_history(import_data(input_test))

for name,expected_balance,date in expected_results:
    balance = get_balance(input_history, name, date)
    assert balance == expected_balance

```

