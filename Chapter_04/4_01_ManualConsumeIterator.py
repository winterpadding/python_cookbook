with open('./4_01_data.txt') as fh:
    try:
        while True:
            line = next(fh)
            print(line, end='')
    except StopIteration:
        pass
