from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """
        Find if an array is good or not.
        An array is good only if it's a permutation of an array base[n], where base[n] = [1, 2, ..., n - 1, n, n].
        For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

        Args:
            nums (List[int]): An integer array to analyze.

        Returns:
            bool: True if the array is good, False otherwise
        """
        base = len(nums) - 1

        if base == 0:
            return False

        nums.sort()
        expected = [num for num in range(1, base + 1)]
        expected.append(base)

        return nums == expected
