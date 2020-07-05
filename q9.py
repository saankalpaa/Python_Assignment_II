array = [8, 19, 22, 31, 45]
item = int(input('enter the item you are looking for: ')) 
from math import floor


def binary_search(array, item):
    n = len(array)
    left = 0
    right = n-1

    while left <= right:
        mid = ((left+right)//2)
        if array[mid] < item:
            left = mid + 1
        elif array[mid] > item:
            right = mid - 1
        else:
            return mid
    return -1

print(binary_search(array, item))