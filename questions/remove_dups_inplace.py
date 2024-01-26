"""Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then
the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums."""
from typing import List

MAX_OUT_DUPS = 2


def remove_dups(nums: List[int]) -> int:
    # reader: int = 0  ## potential dup with i below
    writer: int = 0
    monotonic_val = nums[0]
    seen_val_count: int = 1

    for reader, num in enumerate(nums):
        # look at value, non-decreasing means it must be the same, or greater
        assert num >= monotonic_val, "next is smaller, input violation"

        # if value is greater , than it is "new".
        if num > monotonic_val:
            seen_val_count = 1
            monotonic_val = num
            nums[writer] = num
            writer += 1
        elif num == monotonic_val:
            if seen_val_count < MAX_OUT_DUPS:
                seen_val_count += 1
                nums[writer] = num
                writer += 1
            elif seen_val_count >= MAX_OUT_DUPS:
                continue