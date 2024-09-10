import pytest
from src.hw2_debugging import merge_sort


@pytest.mark.parametrize("x, expected", [
    ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7])])
def test_sort1(x, expected):
    """
    Test merge_sort with a reversed list.
    """
    result = merge_sort(x)
    assert result == expected


@pytest.mark.parametrize("x, expected", [
    ([5, 4, 3, 1, 2, 3, 4], [1, 2, 3, 3, 4, 4, 5])])
def test_sort2(x, expected):
    """
    Test merge_sort with a list containing duplicate values.
    """
    result = merge_sort(x)
    assert result == expected


@pytest.mark.parametrize("x, expected", [
    ([8, 9, 3, 2, 1, 2, 4, 16, 12], [1, 2, 2, 3, 4, 8, 9, 12, 16])])
def test_sort3(x, expected):
    """
    Test merge_sort with a mixed list of integers, including duplicates.
    """
    result = merge_sort(x)
    assert result == expected
