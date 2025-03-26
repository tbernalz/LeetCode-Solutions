from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        Finds the integer that appears more than 25% of the time in a sorted array.

        Args:
            arr (List[int]): The integer array sorted in non-decreasing order.

        Returns:
            int: The element that appears more than 25% of the time. Otherwise return -1.
        """
        quarter = len(arr) // 4

        for i in range(len(arr) - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]

        return -1
