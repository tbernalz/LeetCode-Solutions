from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Calculates the minimum number of decrement operations needed to make the sum
        of the array divisible by k.

        Args:
            nums (List[int]): The integers array.
            k (int): The divisor to check for sum divisibility

        Returns:
            int: The minimum number of operations required
        """
        sum_nums = sum(nums)

        remainder = sum_nums % k

        return remainder
