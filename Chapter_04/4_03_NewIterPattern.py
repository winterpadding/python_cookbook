def float_range(start, stop, increment):
    x = start
    while x <= stop:
        yield x
        x += increment


def countdown(n):
    print(f'Starting to count down from {n}')
    while n > 0:
        yield n
        n -= 1
    print('Done!')


if __name__ == '__main__':
    for n in float_range(0, 4, 0.5):
        print(n)

    c = countdown(3)
    print(c)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))  # Will cause a StopIteration exception
