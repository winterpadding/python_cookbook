import re


def simple(data):
    # r before the string means raw string literals
    pattern = r'[;,\s]\s*'
    fields = re.split(pattern, data)
    print(fields)


def with_delimiters(data):
    pattern = r'(;|,|\s)\s*'
    fields = re.split(pattern, data)
    print(fields)

    values = fields[::2]
    delimiters = fields[1::2] + [''] # Add extra element so it is the same length as the values list
    # If we don't add the empty string to the delimiters list, the zip function used below will omit the
    # last element of the values array

    print(len(values))
    print(len(delimiters))

    recombined = ''.join(v+d for v, d in zip(values, delimiters))
    print(recombined)


def non_capture(data):
    pattern = r'(?:;|,|\s)\s*' # ?: means a non capturing group
    fields = re.split(pattern, data)
    print(fields)


line = 'asdf fjdk; afed, fjek,asdf,     foo'
simple(line)
with_delimiters(line)
non_capture(line)
