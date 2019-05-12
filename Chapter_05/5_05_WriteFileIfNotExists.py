import os


def write_file_after_check_file_exists(filepath):
    if not os.path.exists(filepath):
        with open(filepath, 'wt') as fh:
            fh.write('Hello, World!\n')
    else:
        print(f'File {filepath} already exists')


def write_file_x_mode(filepath):
    try:
        with open(filepath, 'xt') as fh:
            fh.write('Hello, World!\n')
    except FileExistsError:
        print(f'File {filepath} already exists')


path = './5_05_Data.txt'
write_file_after_check_file_exists(path)
write_file_x_mode(path)
