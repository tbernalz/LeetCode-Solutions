class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        """
        Counts the number of times the cumulative sum of steps returns to the origin.

        Args:
            nums(list[int]): A list of integers representing the steps.

        Returns:
            int: The number of times the cumulative sum returns to zero.
        """
        boundary_distance = 0
        result = 0

        for step in nums:
            boundary_distance += step

            if boundary_distance == 0:
                result += 1

        return result
