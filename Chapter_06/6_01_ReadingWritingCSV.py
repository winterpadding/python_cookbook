import csv
from collections import namedtuple
import re


def read_csv_index_position(filepath):
    with open(filepath, 'r') as fh:
        fh_csv = csv.reader(fh)
        heading = next(fh_csv)
        for row in fh_csv:
            print(f"Stock: {row[0]}, Price:{row[1]}")


def read_csv_named_tuple(filepath):
    with open(filepath, 'r') as fh:
        fh_csv = csv.reader(fh)
        headings = next(fh_csv)
        Row = namedtuple('Row', headings)
        for r in fh_csv:
            row = Row(*r)
            print(f"Stock: {row.Symbol}, Price:{row.Price}")


def read_csv_named_tuple_bad_identifiers(filepath):
    def clean_name(name):
        # Note: this will fail if there is a leading space in the header name
        # e.g. Name1, Name2
        # The space between , and N will be converted to an _
        # _Name2 is an invalid value for namedtuple despite it being a valid variable name
        pattern = '[^a-zA-Z_]'
        replace_with = '_'
        return re.sub(pattern, replace_with, name)

    with open(filepath, 'r') as fh:
        fh_csv = csv.reader(fh)
        headings = next(fh_csv)
        headings = [clean_name(h) for h in headings]
        Row = namedtuple('Row', headings)
        for r in fh_csv:
            row = Row(*r)
            print(f"{row}")


def read_csv_dictionary(filepath):
    with open(filepath, 'r') as fh:
        fh_csv = csv.DictReader(fh)
        for row in fh_csv:
            print(row)


stocks_path = './6_01_stocks.csv'
print('Using positions')
read_csv_index_position(stocks_path)

print('Using header as named tuple')
read_csv_named_tuple(stocks_path)

print("Using dictionary")
read_csv_dictionary(stocks_path)

print("Cleaning up invalid names")
premises_path = './6_01_premises.csv'
read_csv_named_tuple_bad_identifiers(premises_path)

