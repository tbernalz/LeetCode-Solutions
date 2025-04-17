from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        """
        Check if a given square matrix follow these two rules:
            1. All the elements in the diagonals of the matrix are non-zero.
            2. All other elements are 0.

        Args:
            grid (List[List[int]]): A 2D array representing a n * n square matrix.

        Returns:
            bool: True if the matrix follow the rules, False otherwise.
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j or abs(i + j) == len(grid) - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False

        return True
