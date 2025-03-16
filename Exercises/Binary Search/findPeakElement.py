from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
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
