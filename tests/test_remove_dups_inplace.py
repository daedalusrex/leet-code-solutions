import pytest

from questions.remove_dups_inplace import remove_dups

dups_test_cases = [
    ([1, 1, 1, 2, 2, 3], [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], [0, 0, 1, 1, 2, 3, 3]),
]


@pytest.mark.parametrize("nums, expected_arr", dups_test_cases)
def test_remove_dups_inplace(nums, expected_arr):
    assert remove_dups(nums) == (len(expected_arr), expected_arr)
