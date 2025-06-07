from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]

#stable
def bubble_sort(nums: List[int]) -> List[int]:
    sortedIndex = 0
    while sortedIndex < len(nums):
        for i in range(len(nums) - 1, sortedIndex, -1):
            if nums[i] < nums[i - 1]:
                tmp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = tmp
        sortedIndex += 1
    return nums

#pre-stop
def bubble_sort_1(nums: List[int]) -> List[int]:
    sortedIndex = 0
    while sortedIndex < len(nums):
        temp = False
        for i in range(len(nums) - 1, sortedIndex, -1):
            if nums[i] < nums[i - 1]:
                tmp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = tmp
                temp = True
        if not temp:
            break
        sortedIndex += 1
    return nums


print(bubble_sort_1(nums))
