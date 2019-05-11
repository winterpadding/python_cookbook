from decimal import Decimal
from decimal import localcontext


def float_fail():
    a = 4.2
    b = 2.1
    print(a+b)
    print((a+b == 6.3))  # Limitation of IEEE754


def decimal_ftw():
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a+b)
    print(a+b == Decimal('6.3'))


def variable_precision(precision):
    a = Decimal('1.3')
    b = Decimal('1.7')
    with localcontext() as ctx:
        ctx.prec = precision
        print(a / b)


float_fail()
decimal_ftw()
variable_precision(3)
variable_precision(50)

# Note: Floats are faster than decimals and often provide sufficient accuracy/precision for general use.

