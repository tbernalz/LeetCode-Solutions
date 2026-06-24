from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum possible difference between the highest and lowest
        scores when choosing any `k` elements from the array.

        Args:
            nums (List[int]): An integer array to analyze.
            k (int): The number of values to select.

        Returns:
            int: The minimum difference between the max and min of the selected values.
        """
        min_diff = float("inf")

        nums.sort()

        for i in range(len(nums)):
            if i + k > len(nums):
                break

            min_diff = min(min_diff, nums[i + k - 1] - nums[i])

        return min_diff
