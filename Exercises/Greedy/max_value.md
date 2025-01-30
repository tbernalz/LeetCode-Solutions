# Maximum Value after Insertion

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-value-after-insertion/description/).

## Initial Approach

I implemented a greedy strategy that aims to maximize the numerical value of the large integer `n` by inserting the digit `x` at the optimal position. The algorithm differentiates between positive and negative numbers to ensure the correct placement of `x`.

- **For positive numbers**: The algorithm iterates through the string representation of `n` and inserts `x` at the first position where the current digit is less than `x`. This ensures that the number is maximized by placing `x` as early as possible.

- **For negative numbers**: The algorithm skips the negative sign and inserts `x` at the first position where the current digit is greater than `x`. This ensures that the number is maximized (the absolute value is minimized) by placing `x` as early as possible.

If no such position is found (`x` is not inserted during the iteration), it is appended to the end of the string.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the string representation of the integer.

- **Space Complexity**: `O(n)`, where n is the length of the string representation of the integer.

  - The algorithm constructs a new string when inserting `x`, which requires additional space proportional to the length of `n`
