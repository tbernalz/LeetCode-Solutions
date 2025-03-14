from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        total_sum = 0
        prev_height = 0

        for height in maximumHeight:
            current_max = height
            assigned_height = min(
                current_max, prev_height - 1 if prev_height > 0 else current_max
            )
            if assigned_height < 1:
                return -1
            total_sum += assigned_height
            prev_height = assigned_height

        return total_sum
