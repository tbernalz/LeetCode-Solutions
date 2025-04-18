from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Finds the single element in a sorted array where every other element appears exactly twice.

        Args:
            nums (List[int]): A sorted array where all elements except one appear exactly twice.

        Returns:
            int: The single element that does not appear twice.
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2

        return nums[left]
