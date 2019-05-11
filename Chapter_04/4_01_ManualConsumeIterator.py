def method_one(filepath):
    with open(filepath) as fh:
        try:
            while True:
                line = next(fh)
                print(line, end='')
        except StopIteration:
            pass


def method_two(filepath):
    with open(filepath) as fh:
        while True:
            line = next(fh, None)
            if line is None:
                break
            print(line, end='')


file = './4_01_data.txt'
print('Method 1')
method_one(file)
print('\n')
print('Method 2')
method_two(file)
