class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum subarray sum of all subarrays of size k with distinct elements.

        Args:
            nums (list[int]): The array to analyze.
            k (int): The required subarray length.

        Returns:
            int: The maximum sum of a valid subarray, or 0 if no valid subarray exists.
        """
        num_set = set()
        max_sum = 0
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in num_set:
                num_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            num_set.add(nums[right])
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                num_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum
