from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Find all possible subsets from the `nums` array without duplicate subsets.

        Args:
            nums (List[int]): The integers array that may contain duplicates elements.

        Returns:
            List[List[int]]: All possible subsets without duplicate subsets.
        """
        result = []
        nums.sort()

        def backtrack(start: int, current: List[int]) -> None:
            result.append(list(current))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])

        return result
