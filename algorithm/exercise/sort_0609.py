from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]

def merge_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    sort(nums, 0, n - 1)
    return nums

def sort(nums:  List[int],lo: int,hi: int):
    if lo==hi:
        return
    mid = (lo+hi)//2
    sort(nums,lo,mid)
    sort(nums,mid+1,hi)
    merge(nums,lo,mid,hi)

def merge(nums:  List[int],lo: int,mid: int,hi: int):
    i,j=lo,mid+1
    temp = [0] * len(nums)
    for x in range(lo,hi+1):
        temp[x] = nums[x]

    for p in range(lo,hi+1):
        if i == mid + 1:
            # 左半边数组已全部被合并
            nums[p] = temp[j]
            j += 1
        elif j == hi + 1:
            # 右半边数组已全部被合并
            nums[p] = temp[i]
            i += 1
        elif temp[i] > temp[j]:
            nums[p] = temp[j]
            j += 1
        else:
            nums[p] = temp[i]
            i += 1

print(merge_sort(nums))