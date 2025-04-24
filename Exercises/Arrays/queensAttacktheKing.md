# Queens That Can Attack the King

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/queens-that-can-attack-the-king/description/).

## Initial Approach

The initial approach involves checking all possible directions from the king's position to find the nearest queen in each direction that can attack the king. The key idea is to explore all 8 possible directions (horizontal, vertical, and diagonal) from the king's position and stop as soon as a queen is encountered in any direction.

1. **Convert Queens to a Set**: First, the positions of the queens are converted into a set for `O(1)` lookups.

1. **Explore Directions**: For each of the 8 possible directions, the algorithm moves step by step away from the king until it either:

   - Goes out of the chessboard bounds (8x8 grid), or encounters a queen.
   - The first queen encountered in each direction is added to the result list since it can attack the king without any blocking pieces.

This approach efficiently narrows down the queens that can attack the king by leveraging the chess rules for queen movement and ensuring no blocking pieces are in the way.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(1)`

  - The chessboard size is fixed (8x8), so the maximum steps taken in any direction is 7. With 8 directions, the total operations are bounded by a constant (8\* 7 = 56), making the time complexity O(1).
  - Also, the `queens` set construction is fixed, since the max length of the `queens` is (8x8)-1 = 63

- **Space Complexity**: `O(1)`
  - The space used is for the set of queen positions, which can be at most 64 (8x8). However, since the board size is fixed, this is considered constant space.
