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
