class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find the indices of two numbers in the list such that they add up to the target.

        Args:
            nums(list): The list of numbers.
            target(int): The target sum.

        Returns:
            list: The list containing the indices of the two numbers that add up to the target.
        """
        hash_nums = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_nums:
                return [hash_nums[complement], i]

            hash_nums[num] = i
