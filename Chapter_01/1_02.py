# NOTE: in the example in the book (p3) the avg function is used
# this didn't work in Python 3.6.1
import statistics
import sys # for the limit of recursion


def drop_first_last(grades):
    first, *middle, last = grades  # This is referred to as "star unpacking"
    avg = statistics.mean(middle)
    print(f"Average grade excluding first and last score: {avg}")


def sales(sales_data):
    *trailing, current = sales_data
    print(f"Trailing: {trailing}")
    print(f"Current: {current}")


def recursive_sum(items):
    head, *tail = items
    return head + recursive_sum(tail) if tail else head


if __name__ == '__main__':
    grades = [12, 45, 56, 23, 75]
    drop_first_last(grades)

    sales_data = [10, 8, 7, 1 , 9, 5, 10, 3]
    sales(sales_data)

    items = [1, 10, 7, 4, 5, 9]
    total = recursive_sum(items)
    print(f"The sum of {items} is {total}")

    print(f"Max recursion depth: {sys.getrecursionlimit()}")