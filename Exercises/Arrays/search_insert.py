class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            check_position = (left + right) // 2

            if nums[check_position] == target:
                return check_position
            elif nums[check_position] > target:
                right = check_position
            else:
                left = check_position + 1

        return left
