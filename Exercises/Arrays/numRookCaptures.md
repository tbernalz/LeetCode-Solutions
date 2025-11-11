# Available Captures for Rook

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/available-captures-for-rook/description/).

## Initial Approach

The approachinvolves two main steps: **Locating the Rook** and **Checking Capture Directions**.

1.  **Locating the Rook:** The entire $8 \times 8$ chessboard (`board`) is iterated over to find the position (row and column index) of the white rook, represented by the character `'R'`. This process terminates as soon as the rook is found.
2.  **Checking Capture Directions:** Once the rook's position is known, the code iterates outwards from this position in the four cardinal directions: up, down, left, and right.
    - For each direction, the iteration stops at the first piece encountered.
    - If the encountered piece is a black pawn (`'p'`), the capture count is incremented by one, and the search in that specific direction terminates.
    - If the encountered piece is a black bishop (`'B'`) or a friendly piece (which would be another `'R'` or an empty square outside the board boundaries, although the code structure handles the boundaries implicitly and ignores the `'R'` itself), the search in that direction terminates without incrementing the count. Empty squares (`'.'`) are simply skipped over.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(1)`, since the size of the `board` is a constant (8x8), so the maximum number of cells to visit is $8 \times 8 = 64$ .

- **Space Complexity**: `O(1)`, since the size of the `board` is a constant (8x8).
