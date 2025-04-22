# Minimum Addition to Make Integer Beautiful

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/description/).

## Initial Approach

The initial approach involves incrementally adjusting the number `n` by the smallest possible increments to ensure the sum of its digits becomes less than or equal to `target`. The strategy is to start from the least significant digit and round up to the next higher place value (e.g., 10, 100, 1000, etc.) whenever the current digit sum exceeds `target`. This ensures that we minimize the increment `x` while systematically reducing the digit sum.

For each iteration, the algorithm:

- Checks if the digit sum of `n` is already <= `target`. If yes, it returns the current `x`.

- Otherwise, it calculates the smallest increment needed to round `n` up to the next multiple of the current place value (`units`).

- Adds this increment to both `n` and `x`, then increases the place value for the next iteration.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(k * log n)`, where k is the number of digits in `n`.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
