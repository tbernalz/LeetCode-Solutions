from typing import List


class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        """
        Calculates the maximum possible total sum of heights for a set of towers, where each tower is assigned a unique height.

        Each tower's height must be a positive integer and cannot exceed its corresponding maximum height limit specified in the "maximumHeight" array.
        Additionally, no two towers can have the same height. If it's not possible to assign unique heights under these constraints, the function returns -1.

        Args:
            maximumHeight (List[int]): A list of integers where each element "maximumHeight[i]" represents the maximum allowable height for the ith tower.

        Returns:
            int: The maximum possible total sum of the heights of all towers if unique heights can be assigned, otherwise returns -1.
        """
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
