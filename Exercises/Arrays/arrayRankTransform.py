from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        Rank all elemens from arr following these rules:
            - Rank is an integer starting from 1.
            - The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
            - Rank should be as small as possible.

        Args:
            arr (List[int]): An integer array to analyze.

        Returns:
            List[int]: The ranking.
        """
        ranking = [0] * len(arr)
        current_rank = 0
        prev_value = None

        indexed_arr = [(value, i) for i, value in enumerate(arr)]
        indexed_arr.sort()

        for value, i in indexed_arr:
            if value != prev_value:
                current_rank += 1
                prev_value = value
            ranking[i] = current_rank

        return ranking
