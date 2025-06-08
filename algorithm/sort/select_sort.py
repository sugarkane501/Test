from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]

# unstable
def select_sort(nums: List[int]) -> List[int]:
    sortedIndex = 0
    while sortedIndex < len(nums):
        minIndex = sortedIndex
        for i in range(sortedIndex, len(nums)):
            if nums[i] < nums[minIndex]:
                minIndex = i
        nums[minIndex], nums[sortedIndex] = nums[sortedIndex], nums[minIndex]
        sortedIndex += 1
    return nums


# stable
def select_sort_1(nums: List[int]) -> List[int]:
    sortedIndex = 0
    while sortedIndex < len(nums):
        minIndex = sortedIndex
        for i in range(sortedIndex, len(nums)):
            if nums[i] < nums[minIndex]:
                minIndex = i
        min_value = nums[minIndex]
        while minIndex > sortedIndex:
            nums[minIndex] = nums[minIndex - 1]
            minIndex -= 1
        nums[sortedIndex] = min_value
        sortedIndex += 1
    return nums


print(select_sort_1(nums))
