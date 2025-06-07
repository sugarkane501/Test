# Sorting the element when traverse on the binary-tree's pre-position
from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]


def start(nums: List[int]):
    n = len(nums)
    fast_sort(nums, 0, n - 1)
    print(nums)


def fast_sort(nums: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    p = partition(nums, lo, hi)

    fast_sort(nums, lo, p - 1)
    fast_sort(nums, p + 1, hi)


def partition(nums: List[int], lo: int, hi: int):
    pivot = nums[lo]
    i, j = lo + 1, hi
    while i <= j:
        while i < hi and nums[i] <= pivot:
            i += 1

        while j > lo and nums[j] > pivot:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[lo], nums[j] = nums[j], nums[lo]
    return j


start(nums)
