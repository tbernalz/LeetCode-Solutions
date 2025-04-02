from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        """
        Return the sum of elements in the array strictly greater than their left and right neighbors at distance `k` (if they exist).

        Args:
            nums (List[int]): An array of integers.
            k (int): The distance to check for neighboring elements.

        Returns:
            int: The sum of all good numbers in the array.
        """
        total = 0

        for i in range(len(nums)):
            is_good = True
            if i - k >= 0 and nums[i] <= nums[i - k]:
                is_good = False
            if i + k < len(nums) and nums[i] <= nums[i + k]:
                is_good = False
            if is_good:
                total += nums[i]
        return total
