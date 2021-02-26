#!/usr/bin/env python3

"""Sampler

Generate sample data (exchanges,revenues,expenses)
for ledger in a csv format and redirects as string to stdout

Examples:
    sampler.py
    sampler.py > random.csv
    sampler.py -l 10 > random30.csv

Usage:
    sampler.py [-l=<line_nb>]
    sampler.py (-h | --help)
    sampler.py (-v |--version)

Options:
    -h --help       Show this screen.
    -v --version    Show version.
    -l=<line_nb>    Number of lines to generate x3 [default: 50].

Displays:
    multilines coma separated string.

Returns:
    None
"""

import datetime
import random

from docopt import docopt


def generate_random_day(start=(2015, 1, 1), end=(2020, 3, 1)):
    """
    Generate a random day from start day to end day
    Returns a string representation of the day
    into following format "YYYY-MM-dd"
    """
    start_day = datetime.date(*start)
    end_day = datetime.date(*end)
    time_between_dates = end_day - start_day
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_day + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


def generate_data(nb_row=50):
    """
    Generate data transaction of 3 kinds:
    - account_name
    - expenses
    - revenues
    into a
    """
    names = ["john", "mary", "suzy", "joe", "weifang", "claire"]
    expenses = ["insurance", "supermarket", "internet"]
    revenues = ["job", "poker", "legacy"]
    data = []
    for nb in range(nb_row):
        chosen_names = random.sample(names, 2)
        amount = round(random.uniform(1, 500), 2)
        day = generate_random_day()
        row = [day, chosen_names[0], chosen_names[1], str(amount)]
        data.append(row)
    for nb in range(nb_row):
        name = random.sample(names, 1)
        amount = round(random.uniform(1, 500), 2)
        day = generate_random_day()
        expense = random.sample(expenses, 1)
        data.append([day, name[0], expense[0], str(amount)])
    for nb in range(nb_row):
        name = random.sample(names, 1)
        amount = round(random.uniform(1, 500), 2)
        day = generate_random_day()
        revenue = random.sample(revenues, 1)
        data.append([day, revenue[0], name[0], str(amount)])
    sorted_data = sorted(data, key=lambda x: x[0])
    return "\n".join([",".join(row) for row in sorted_data])


if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0")
    print(generate_data(int(arguments["-l"])))
