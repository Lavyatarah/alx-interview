#!/usr/bin/python3

"""Import some modules"""

import sys

"""create a function that takes file size and status"""


def _print(total_file_size, status):
    """function to print total file size and status codes"""
    print("File size: {:d}".format(total_file_size))
    for key, value in sorted(statuses.items()):
        if value != 0:
            print("{}: {}".format(key, value))


statuses = {
        '200': 0, '301': 0,
        '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

total_file_size = 0
count = 0
try:
    for line in sys.stdin:
        args = line.split()

        if len(args) > 2:
            status_code = args[-2]
            file_size = int(args[-1])

            if status_code in statuses:
                statuses[status_code] += 1

            total_file_size += file_size
            count += 1

            if count == 10:
                _print(total_file_size, statuses)
                count = 0

except KeyboardInterrupt:
    pass

finally:
    _print(total_file_size, statuses)
