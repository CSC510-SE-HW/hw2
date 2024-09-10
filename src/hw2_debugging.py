"""
Module for implementing of Merge Sort Algorithm
"""
from src import rand


def merge_sort(input_arr):
    """
    Perform a merge sort on the input array.

    Args:
        input_arr (list): The array to be sorted.

    Returns:
        list: Sorted array.
    """
    if len(input_arr) <= 1:
        return input_arr

    half = len(input_arr) // 2
    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombine two sorted arrays into one sorted array.

    Args:
        left_arr (list): The left sorted array.
        right_arr (list): The right sorted array.

    Returns:
        list: Merged sorted array.
    """
    left_index = 0
    right_index = 0
    merged_arr = []

    # Merge two arrays
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merged_arr.append(right_arr[right_index])
            right_index += 1

    # Append remaining elements from both arrays
    merged_arr.extend(left_arr[left_index:])
    merged_arr.extend(right_arr[right_index:])

    return merged_arr


# Generate a random array and perform merge sort
random_arr = rand.random_array([None] * 20)
sorted_arr = merge_sort(random_arr)

print(sorted_arr)
