from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Find all possible subsets from the `nums` array without duplicate subsets.

        Args:
            nums (List[int]): The array of unique integers.

        Returns:
            List[List[int]]: All possible subsets without duplicate subsets.
        """
        result = []

        def backtrack(start: int, current: List[int]) -> None:
            result.append(list(current))
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])

        return result
