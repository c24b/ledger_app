#!/usr/bin/env python


import pytest
import subprocess


from ledger import import_data
from ledger import build_history
from ledger import get_balance



def test_001_import_data():
    """
    Test import_data facility
    """
    with open("example.csv", "r") as f:
        sample_data = f.read() 
    history = import_data(sample_data)
    assert isinstance(history, list)
    assert history[0][-1] == "125.00"
    history = import_data(
        """2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00
    """
    )
    assert isinstance(history, list)
    assert history[0][-1] == "125.00"
    history = import_data(
        """day,giver,receiver,amount
2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00
    """
    )
    assert isinstance(history, list)
    assert history[1][-1] == "20.00"
    with open("example_with_header.csv", "r") as f:
        sample_data = f.read()
    history = import_data(sample_data)
    assert isinstance(history, list)
    assert history[-1][-1] == "100.00"
    with pytest.raises(TypeError):
        history = import_data([])
    with pytest.raises(TypeError):
        history = import_data("""""")
    with pytest.raises(TypeError):
        history = import_data(12)


def test_002_build_history():
    with open("example.csv", "r") as f:
        sample_data = f.read()
    history = build_history(import_data(sample_data))
    assert isinstance(history, dict)
    assert isinstance(list(history.keys())[0], str)
    assert isinstance(list(history.values())[0][0][0], float)
    assert (list(history.values())[0][0][1]).count("-") == 2


def test_003_get_balance():
    """test balance with sample data given"""
    with open("example.csv", "r") as f:
        sample_data = f.read()
    history = build_history(import_data(sample_data))
    print(history)
    assert get_balance(history, "insurance") == 100
    assert get_balance(history, "john") == -145.00
    assert get_balance(history, "mary", "2015-01-01") == 0
    assert get_balance(history, "mary", "2015-01-16") == 125
    assert get_balance(history, "mary", "2015-01-17") == 25
    assert get_balance(history, "supermarket", "2015-01-16") == 0
    assert get_balance(history, "supermarket") == 20
    assert get_balance(history, "supermarket", "2015-01-17") == 20
    with pytest.raises(KeyError):
        assert get_balance(history, "claire")


def test_004_app():
    cmd = "python ledger.py john -i example.csv".split(" ")
    output = subprocess.check_output(cmd).decode("utf-8").strip()
    display = [n.strip() for n in output.split("\n")]
    assert display[-1] == "2015-01-17	john	-145.00 §"
    cmd = "python ledger.py john -i example.csv --date=2015-01-15".split(" ")
    output = subprocess.check_output(cmd).decode("utf-8").strip()
    display = [n.strip() for n in output.split("\n")]
    assert display[-1] == "2015-01-15	john	0.00 §"
