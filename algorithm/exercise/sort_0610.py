from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]


def insert_sort(nums: List[int]) -> List[int]:
    sortedIndex = 0
    n = len(nums)
    while sortedIndex < n:
        for i in range(sortedIndex, 0, -1):
            if nums[i - 1] > nums[i]:
                tmp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = tmp
            else:
                break
        sortedIndex += 1
    return nums


def fast_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    sort(nums, 0, n - 1)
    return nums


def sort(nums: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    p = partition(nums, lo, hi)

    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)


def partition(nums: List[int], lo: int, hi: int):
    pivot = nums[lo]
    i, j = lo + 1, hi
    while i < j:
        while i < hi and nums[i] < pivot:
            i += 1
        while j >= lo and nums[j] > pivot:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[lo], nums[j] = nums[j], nums[lo]
    return j


def merge_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    sort_1(nums, 0, n - 1)
    return nums


def sort_1(nums: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    mid = (lo + hi) // 2

    sort_1(nums, lo, mid)
    sort_1(nums, mid + 1, hi)
    merge(nums, lo, mid, hi)


def merge(nums: List[int], lo: int, mid: int, hi: int):
    i, j = lo, mid + 1
    temp = [0] * len(nums)
    for x in range(lo, hi + 1):
        temp[x] = nums[x]

    for p in range(lo, hi + 1):
        if i == mid + 1:
            nums[p] = temp[j]
            j += 1
        elif j == hi + 1:
            nums[p] = temp[i]
            i += 1
        elif temp[i] > temp[j]:
            nums[p] = temp[j]
            j += 1
        else:
            nums[p] = temp[i]
            i += 1


print(merge_sort(nums))
