from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible unique permutations of an array of distinct integers.

        Args:
            nums (List[int]): An array of distinct integers for which permutations are to be generated.

        Returns:
            List[List[int]]: All the possible permutations.
        """

        def backtrack(path: List[int], remaining: List[int]) -> None:
            if not remaining:
                result.append(path.copy())
                return

            for i in range(len(remaining)):
                remaining[0], remaining[i] = remaining[i], remaining[0]
                path.append(remaining[0])
                backtrack(path, remaining[1:])
                path.pop()
                remaining[0], remaining[i] = remaining[i], remaining[0]

        result = []
        backtrack([], nums)

        return result
