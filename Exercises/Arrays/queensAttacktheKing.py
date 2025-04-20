from typing import List


class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        """
        Finds all black queens that can directly attack the white king on an 8x8 chessboard.

        A queen can directly attack the king if:
        1. They share the same row, column, or diagonal, and
        2. There are no other pieces blocking the path between them.

        Args:
            queens (List[List[int]]): A 2D integer array representing black queens' positions.
            king (List[int]): A integer array representing the white king's position.

        Returns:
            List[List[int]]: The positions of the queens that can directly attack the king.
        """
        result = []
        queensSet = {(i, j) for i, j in queens}
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
        ]

        for dx, dy in directions:
            king_x = king[0]
            king_y = king[1]

            while True:
                king_x += dx
                king_y += dy

                if not (0 <= king_x < 8 and 0 <= king_y < 8):
                    break
                if (king_x, king_y) in queensSet:
                    result.append([king_x, king_y])
                    break

        return result
