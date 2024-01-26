"""Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then
the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums."""
from typing import List, Tuple, Final

MAX_OUT_DUPS: Final[int] = 2


def remove_dups(nums: List[int]) -> Tuple[int, List[int]]:
    # Stupid Edge Case
    if len(nums) == 1:
        return len(nums), nums

    writer: int = 1  # Writer starts at i:1 because 0th is always present
    monotonic_val = nums[0]
    seen_val_count: int = 1

    for reader, num in enumerate(nums):
        # look at value, non-decreasing means it must be the same, or greater
        assert num >= monotonic_val, "next is smaller, input violation"

        # Edge case, don't read the first one because always present
        if reader == 0:
            continue

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

    return writer, nums[0:writer]
