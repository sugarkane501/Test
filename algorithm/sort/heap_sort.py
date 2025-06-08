from typing import List

nums = [3, 4, 1, 5, 9, 2, 1, 6]


def min_heap_swim(heap, node):
    while node > 0 and heap[node] < heap[parent(node)]:
        swap(heap, node, parent(node))
        node = parent(node)


def min_heap_sink(heap, node, size):
    while left(node) < size or right(node) < size:
        min_index = node
        if left(node) < size and heap[min_index] > heap[left(node)]:
            min_index = left(node)
        if right(node) < size and heap[min_index] > heap[right(node)]:
            min_index = right(node)
        if min_index == node:
            break
        swap(heap, min_index, node)
        node = min_index


def max_heap_swim(heap, node):
    while node > 0 and heap[node] > heap[parent(node)]:
        swap(heap, node, parent(node))
        node = parent(node)


def max_heap_sink(heap, node, size):
    while left(node) < size or right(node) < size:
        max_index = node
        if left(node) < size and heap[max_index] < heap[left(node)]:
            max_index = left(node)
        if right(node) < size and heap[max_index] < heap[right(node)]:
            max_index = right(node)
        if max_index == node:
            break
        swap(heap, node, max_index)
        node = max_index


def left(node):
    return 2 * node + 1


def right(node):
    return 2 * node + 2


def parent(node):
    return (node - 1) // 2


def swap(heap, i, j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp


def heap_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        max_heap_swim(nums, i)
    heap_size = len(nums)
    while heap_size > 0:
        swap(nums, 0, heap_size - 1)
        heap_size -= 1
        max_heap_sink(nums, 0, heap_size)
    return nums


print(heap_sort(nums))
