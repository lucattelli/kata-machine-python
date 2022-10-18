import math


def binary_search(haystack: list[int], needle: int) -> bool:

    haystack_size = len(haystack)
    low = 0
    high = haystack_size

    while low < high:
        middle = math.floor(low + (high - low) / 2)
        value = haystack[middle]

        if value == needle:
            return True
        elif value > needle:
            high = middle
        else:
            low = middle + 1

    return False
