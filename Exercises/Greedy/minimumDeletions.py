from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        """
        Calculat the minimum number of deletions it would take to remove both the minimum and maximum element from the array.
        A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

        Args:
            nums (List[int]): The integer array.

        Returns:
            int: The minimum number of deletions required.
        """

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        option1 = max_index + 1
        option2 = len(nums) - min_index
        option3 = (min_index + 1) + (len(nums) - max_index)

        return min(option1, option2, option3)
