import pytest

from questions.remove_dups_inplace import remove_dups

dups_test_cases = [
    ([1, 1, 1, 2, 2, 3], 5),  # [1,1,2,2,3,_]
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),  # [0,0,1,1,2,3,3,_,_]
]


@pytest.mark.parametrize("nums, expected_k", dups_test_cases)
def test_remove_dups_inplace(nums, expected_k):
    assert remove_dups(nums) == expected_k
