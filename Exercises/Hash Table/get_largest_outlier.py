class Solution:
    def getLargestOutlier(self, nums: list[int]) -> int:
        """
        Given an array that contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.
        An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

        Args:
            nums(list[int]): The array to analyze.

        Returns:
            int: The largest potential outlier in nums.
        """
        total_sum = sum(nums)
        nums_set = set(nums)
        largest_outlier = float("-inf")

        for num in nums:
            target = total_sum - (2 * num)
            if target in nums_set and nums.count(target) > (1 if target == num else 0):
                largest_outlier = max(largest_outlier, target)

        return largest_outlier
