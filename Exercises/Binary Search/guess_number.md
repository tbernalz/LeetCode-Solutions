# Guess Number Higher or Lower

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/guess-number-higher-or-lower/description/).

## Initial Approach

aaaaaaaaaaa

## Optimized Solution

The initial approach uses a binary search strategy to efficiently find the target number within the range [1, `n`]. The algorithm works by repeatedly dividing the search range in half and using the guess() API to determine whether the guessed number is higher, lower, or equal to the target.

## Complexity

- **Time Complexity**: `O(log n)`, where n is the upper bound of the range.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
