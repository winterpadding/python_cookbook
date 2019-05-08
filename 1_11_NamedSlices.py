def shares():
    ######   '012345678901234567890123456789012345678901234567890123456789'
    record = '....................100          .......513.23     .........'

    # Naive approach would be to hard code positions
    cost = int(record[20:32]) * float(record[40:48])
    print(cost)

    SHARES = slice(20, 32)
    PRICE = slice(40, 48)

    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)


def discussion():
    items = list('abcdefg')  # Using letters instead of numbers

    print(items)

    sl = slice(2, 4)
    print(items[sl])

    del items[sl]
    print(items)

    print(sl)  # A slice object has a start, stop and step size


def limit_slice():
    s = 'HelloWorld'
    a = slice(5, 50, 2)  # Start at 5, stop at 50, step size = 2
    print(a)

    print(a.indices(len(s)))


if __name__ == '__main__':
    shares()

    discussion()

    limit_slice()