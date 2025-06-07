from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]


# unstable
# in-place sort
def shell_sort(nums: List[int]) -> List[int]:
    h = 1
    n = len(nums)
    while h < n // 2:
        h = 2 * h

    while h >= 1:
        sortedIndex = h
        while sortedIndex < n:
            i = sortedIndex
            while i >= h:
                if nums[i] < nums[i - h]:
                    tmp = nums[i]
                    nums[i] = nums[i - h]
                    nums[i - h] = tmp
                i -= h
            sortedIndex += 1
        h //= 2
    return nums


print(shell_sort(nums))
