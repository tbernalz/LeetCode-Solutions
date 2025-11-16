from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        """
        Calculates the number of pawns ('p') a white rook ('R') can capture in one
        move on an 8x8 chessboard represented by a list of strings.

        Args:
            board(List[List[str]]): A list of 8 lists of strings, where each string
            is a single character representing a square on the 8x8 chessboard.

        Returns:
            The total number of pawns the white rook can capture in one move.
        """
        rook_position = []
        result = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    rook_position = [i, j]
                    break

        for i in range(rook_position[0], -1, -1):
            if board[i][rook_position[1]] == "p":
                result += 1
                break

            elif board[i][rook_position[1]] == "B":
                break

        for i in range(rook_position[0], len(board)):
            if board[i][rook_position[1]] == "p":
                result += 1
                break

            elif board[i][rook_position[1]] == "B":
                break

        for i in range(rook_position[1], len(board)):
            if board[rook_position[0]][i] == "p":
                result += 1
                break

            elif board[rook_position[0]][i] == "B":
                break

        for i in range(rook_position[1], -1, -1):
            if board[rook_position[0]][i] == "p":
                result += 1
                break

            elif board[rook_position[0]][i] == "B":
                break

        return result
