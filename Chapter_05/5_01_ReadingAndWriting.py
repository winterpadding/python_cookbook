import sys


def read_file_utf(filepath):
    with open(filepath, 'rt', encoding='utf-8', newline='') as fh:
        line = fh.read()
        print(line)


def read_file_ascii_replace(filepath):
    with open(filepath, 'rt', encoding='ascii', errors='replace') as fh:
        line = fh.read()
        print(line)


def read_file_ascii_ignore(filepath):
    with open(filepath, 'rt', encoding='ascii', errors='ignore') as fh:
        line = fh.read()
        print(line)


print(sys.getdefaultencoding())
path = './5_01_Data.txt'

read_file_utf(path)
read_file_ascii_replace(path)
read_file_ascii_ignore(path)
