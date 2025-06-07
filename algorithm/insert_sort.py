from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]

# The higher the initial orderliness, the higher the efficiency
def insert_sort(nums: List[int]) -> List[int]:
    sortedIndex = 0
    lens = len(nums)
    while sortedIndex < lens:
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
