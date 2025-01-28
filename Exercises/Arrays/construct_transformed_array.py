class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        """
        Transform an array based on some circular movement rules.

        Args:
            nums(list[int]): The array representing a circular array.

        Returns:
            list[int]: The transformed array.
        """
        len_nums = len(nums)
        result = [None] * len_nums

        for i in range(len_nums):

            if nums[i] > 0:
                position = (i + nums[i]) % len_nums
                result[i] = nums[position]
            elif nums[i] < 0:
                position = (i + nums[i]) % len_nums
                result[i] = nums[position]
            else:
                result[i] = nums[i]

        return result
