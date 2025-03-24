from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        """
        Check if the elements of an integer array can be divided into exact pairs.

        Args:
            nums (List[int]): The array to check for pairs.

        Returns:
            bool: True if all elements can be paired, False otherwise.
        """
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return not seen
