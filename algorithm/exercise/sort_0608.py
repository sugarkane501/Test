from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]


def insert_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    sortedIndex = 0
    while sortedIndex < n:
        for i in range(sortedIndex, 0, -1):
            if nums[i] < nums[i - 1]:
                tmp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = tmp
            else:
                break
        sortedIndex += 1
    return nums


print(insert_sort(nums))


def fast_sort(nums: List[int]) -> List[int]:
    lo, hi = 0, len(nums) - 1
    sort(nums, lo, hi)
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
    while i <= j:
        while i < hi and nums[i] <= pivot:
            i += 1
        while j > lo and nums[j] > pivot:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[j], nums[lo] = nums[lo], nums[j]
    return j

print(fast_sort(nums))
