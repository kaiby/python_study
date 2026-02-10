"""
example04 - 

Author: kaiby
Date: 2024/1/8 16:49
"""


def search(items: list, key) -> int:
    start, end = 0, len(items) - 1

    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(search([1, 2, 3, 4, 5], 13))
