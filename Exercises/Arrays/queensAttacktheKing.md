# Queens That Can Attack the King

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/queens-that-can-attack-the-king/description/).

## Initial Approach

aaaaaaaaa

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(1)`

  - The chessboard size is fixed (8x8), so the maximum steps taken in any direction is 7. With 8 directions, the total operations are bounded by a constant (8\* 7 = 56), making the time complexity O(1).
  - Also, the `queens` set construction is fixed, since the max length of the `queens` is (8x8)-1 = 63

- **Space Complexity**: `O(1)`
  - The space used is for the set of queen positions, which can be at most 64 (8x8). However, since the board size is fixed, this is considered constant space.
