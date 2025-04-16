from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Finds the duplicate number and missing number in a corrupted set of integers from 1 to n.

        The set originally contains all numbers from 1 to n, but due to an error:
        - One number is duplicated (appears twice)
        - One number is missing

        Args:
            nums (List[int]): The corrupted array of integers.

        Returns:
            List[int]: A list containing two elements:
                      - First element: the duplicated number
                      - Second element: the missing number
        """
        duplicate = -1
        missing = -1

        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]
