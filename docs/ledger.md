Ledger

Given a string data stream returns balance of the given account __<name>__

Examples:
    ledger.py john -i example.csv
    cat example.csv | python ledger.py mary
    cat example.csv | python ledger.py mary --date=2015-01-16
    cat example.csv | python ledger.py mary --date=2015-01-17
    echo "2015-01-16,john,mary,125.00
2015-01-17,john,supermarket,20.00
2015-01-17,mary,insurance,100.00" | python ledger.py john

Usage:
  ledger.py __<name>__ [--date=__<date>__]
  ledger.py __<name>__ [-i=__<input_file>__] [--date=__<date>__]
  ledger.py (-h | --help)
  ledger.py (-v |--version)

Options:
  -h --help         Show this screen.
  --version         Show version.
  --date=__<date>__     Specify date of the transaction: YYYY-MM-dd (default:None).
  -i=__<input_file>__   Specify input file (CSV file)

Returns:
    balance (float)

Displays:
    1. All transactions mentionning the given account __<name>__
    2. Balance of the given account __<name>__ at the select __<date>__
    (default to last date of the ledger)
