def coords():
    p = (4, 5)
    x, y = p
    print(f"x: {x}")
    print(f"y: {y}")


def shares(data):
    name, shares_owned, price, date = data
    print(f"name: {name}")

    # Full unpack of nested items
    name, shares_owned, price, (year, month, day) = data
    print(f"year: {year}")


def discard(data):
    # Note that python doesn't have any special syntax for ignoring items.
    # By convention, use _ to denote these discarded items
    _, shares_owned, price, _ = data
    print(f"Shares: {shares_owned}")


if __name__ == '__main__':
    coords()

    share_data = ['ACME', 50, 9.1, (2012, 12, 21)]

    shares(share_data)

    discard(share_data)
