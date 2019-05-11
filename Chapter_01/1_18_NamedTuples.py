from collections import namedtuple


def subby():
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')

    print(sub)

    print(len(sub))

    addr, joined = sub
    print(addr)
    print(joined)


def stock():
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

    # Create a prototype
    stock_prototype = Stock('', 0, 0.0, None, None)

    def convert_stock_dict_to_stock_tuple(s):
        return stock_prototype._replace(**s)

    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(convert_stock_dict_to_stock_tuple(a))


subby()
stock()
