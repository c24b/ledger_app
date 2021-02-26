#!/usr/bin/env python3

"""Ledger

Given a string data stream returns balance of the given account <name>

Examples:
    ledger.py john -i example.csv
    cat example.csv | python ledger.py mary
    cat example.csv | python ledger.py mary --date=2015-01-16
    cat example.csv | python ledger.py mary --date=2015-01-17
    echo "2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00" | python ledger.py john

Usage:
  ledger.py <name> [--date=<date>]
  ledger.py <name> [-i=<input_file>] [--date=<date>]
  ledger.py (-h | --help)
  ledger.py (-v |--version)

Options:
  -h --help         Show this screen.
  --version         Show version.
  --date=<date>     Specify date of the transaction: YYYY-MM-dd (default:None).
  -i=<input_file>   Specify input file (CSV file)

Returns:
    balance (float)

Displays:
    1. All transactions mentionning the given account <name>
    2. Balance of the given account <name> at the select <date>
    (default to last date of the ledger)
"""


import datetime
import sys

from docopt import docopt


def import_data(csv_data):
    """
    Import csv_data from raw str
    using , as cell delimiter and \n as line delimiter
    ```
    date,namex,namey,amount
    date,namez,namey,amount
    date,namey,namea,amount
    ```
    Returns data matrix
    ```
    [
        (dt_str, x,y,float_str),
        (dt_str, x,y,float_str),
        (dt_str, x,y,float_str)
    ]
    ```
    """
    if isinstance(csv_data, str):
        if "\n" in csv_data and "," in csv_data:
            data = [line.split(",") for line in csv_data.split("\n")]
        else:
            raise TypeError("<csv_data>: must be a filename or str.")
    else:
        raise TypeError("<csv_data>: must be a str.")
    if data == []:
        raise TypeError("Wrong format for input data.")
    # remove header if needed
    try:
        # test if last cell of 1st line is an amount
        float(data[0][-1])
    except ValueError:
        # remove header
        del data[0]
    return data


def build_history(matrix):
    """
    Given a matrix: [(date, x,y,amount_str), (...), ... ]
    Return history dict: {name:[[amount_float, date], ...}
    """
    debits = {k: [] for k in set([n[1] for n in matrix])}
    credits = {k: [] for k in set([n[2] for n in matrix])}
    history = {**credits, **debits}
    # sort ledge date by alphabetical order as date format is compatible
    for ledge in sorted(matrix, key=lambda x: x[0]):
        try:
            # cast amount into float
            amount = float(ledge[-1])
        except TypeError:
            raise TypeError("`{}` must be an int or a float".format(amount))
        history[ledge[2]].append((amount, ledge[0]))
        # cast amount into negative float (debit)
        history[ledge[1]].append((-(amount), ledge[0]))
    return history


def get_balance(history, name, date=None):
    """
    Returns balance of <name>.

    Keyword arguments:
    date -- day represented as str following "Y-%m-%d" (default None)
    """
    if date is None:
        try:
            balance = sum([n[0] for n in history[name]])
            date = history[name][-1][1]
        except KeyError:
            raise KeyError("{} not found in transactions".format(name))
    else:
        try:
            date_time_str = date + " 00:00:00"
            dt = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        except AssertionError:
            raise KeyError("Wrong date format :'{}'".format(date))
        try:
            balance = sum([n[0] for n in history[name] if n[1] <= date])
        except KeyError:
            raise KeyError("{} not found in transaction records".format(name))
    balance = round(balance, 2)
    print("\n=== BALANCE: {} ===".format(name))
    print("day\taccount name\tbalance (§)")
    print("\t".join([date, name, "{:.2f} §".format(balance)]))
    return balance




def read_input():
    """
    Catch input from stdin
    """
    lines = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped:
            break
        lines.append(stripped)
    return "\n".join(lines)


def display_transaction_of(name, input_data):
    """
    Display all the transactions for the given <name>
    """
    print("\n=== TRANSACTIONS: {} ===".format(name))
    for line in sorted(input_data.split("\n")):
        if name in line:
            print(line)


def app(arguments):
    if arguments["-i"] is None:
        # check if stdin is provided
        if sys.stdin.isatty():
            print("ERROR: No input provided.")
            print(__doc__)
            raise Exception("Missing input.")
        else:
            input_data = read_input()
    else:
        with open(arguments["-i"], "r") as f:
            input_data = f.read()
    display_transaction_of(arguments["<name>"], input_data)
    history = build_history(import_data(input_data))
    return get_balance(history, arguments["<name>"], arguments["--date"])


if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0")
    app(arguments)
