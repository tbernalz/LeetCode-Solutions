from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        """
        Find a peak element in a given array of integers.

        A peak element is an element that is strictly greater than its neighbors. For elements at the boundaries
        of the array (i.e., the first and last elements), they are considered greater than their non-existent
        neighbors (imagined as -∞). If the array contains multiple peaks, the index of any one of the peaks
        can be returned.

        Args:
            nums (List[int]): A 0-indexed integer array where a peak element is to be found.

        Returns:
            int: The index of a peak element in the array.
        """
        left = 0
        right = len(nums) - 1

        while (right - left) > 1:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid + 1]:
                right = mid
            else:
                left = mid

        if nums[left] > nums[right]:
            return left

        return right
