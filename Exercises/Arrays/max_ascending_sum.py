class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        """Calculates the maximum possible sum of an ascending subarray in an array.

        Args:
            nums(list[int]): The list with the numbers to sum.

        Returns:
            int: The maximum possible sum.
        """
        result = nums[0]
        helper = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                helper += nums[i]

            else:
                helper = nums[i]

            result = max(result, helper)

        return result
