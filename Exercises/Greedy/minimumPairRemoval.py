from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        Finds the minimum operations to make the array non-decreasing by merging adjacent pairs.

        In each operation:
        1. Select the leftmost pair of adjacent elements with the smallest sum
        2. Replace them with their sum

        Args:
            nums (List[int]): The integer array to process.

        Returns:
            int: The minimum number of merge operations required to make the array non-decreasing.
        """
        count = 0

        while True:
            is_non_decreasing = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    is_non_decreasing = False
                    break

            if is_non_decreasing:
                break

            min_index = 0
            min_sum = float("inf")

            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_index = i
                    min_sum = current_sum
            nums = nums[:min_index] + [min_sum] + nums[min_index + 2 :]
            count += 1

        return count
