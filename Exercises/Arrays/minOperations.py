from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Calculate the minimum number of operations needed to make an array strictly increasing.
        The only operation allowed is incrementing an element by 1.

        Args:
            nums (List[int]): The input array to make strictly increasing.

        Returns:
            int: The number of operations needed to make the array strictly increasing.
        """
        operations = 0

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                increment = nums[i - 1] - nums[i] + 1
                operations += increment
                nums[i] += increment

        return operations
