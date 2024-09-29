"""
Test the merge sort algorithm using pytest
"""

import pytest
from src.hw2_debugging import merge_sort

@pytest.mark.parametrize("x, expected", [
    ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]),
], ids=["Reversed list"])
def test_sort_reversed(x, expected):
    """
    Test merge_sort with a reversed list.
    """
    result = merge_sort(x)
    assert result == expected, f"Expected sorted list to be {expected}, but got {result}"

@pytest.mark.parametrize("x, expected", [
    ([5, 4, 3, 1, 2, 3, 4], [1, 2, 3, 3, 4, 4, 5]),
], ids=["List with duplicates"])
def test_sort_duplicates(x, expected):
    """
    Test merge_sort with a list containing duplicate values.
    """
    result = merge_sort(x)
    assert result == expected, f"Expected sorted list to be {expected}, but got {result}"

@pytest.mark.parametrize("x, expected", [
    ([8, 9, 3, 2, 1, 2, 4, 16, 12], [1, 2, 2, 3, 4, 8, 9, 12, 16]),
], ids=["Mixed list with duplicates"])
def test_sort_mixed(x, expected):
    """
    Test merge_sort with a mixed list of integers, including duplicates.
    """
    result = merge_sort(x)
    assert result == expected, f"Expected sorted list to be {expected}, but got {result}"
