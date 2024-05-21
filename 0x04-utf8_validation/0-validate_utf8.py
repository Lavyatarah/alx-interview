#!/usr/bin/python3

"""create a function"""


def validUTF8(data):
    """function that determines if a dataset is valid UTF-8 encoding"""
    count = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7

        if count == 0:
            while mask & num:
                count += 1
                mask >>= 1

            if count == 1 or count > 4:
                return False
            elif count == 0:
                continue
        else:
            if not (num & mask1) or (num & mask2):
                return False
        count -= 1
    return count == 0
