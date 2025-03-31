from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Find the maximum length of a chain of pairs that can be formed.
        A chain is formed by selecting pairs where each subsequent pair starts after the previous one ends.
        The pairs can be selected in any order (they do not need to be contiguous in the original array).

        Args:
            pairs (List[List[int]]): A list of pairs, where each pair is represented as [a, b] with a < b.

        Returns:
            int: The length of the longest possible chain of pairs.
        """
        pairs.sort(key=lambda x: x[1])

        current_end = float("-inf")
        counter = 0

        for pair in pairs:
            if pair[0] > current_end:
                counter += 1
                current_end = pair[1]

        return counter
