# Minimum Pair Removal to Sort Array I

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/).

## Initial Approach

The initial approach involves iteratively checking if the array is non-decreasing. If it is not, the algorithm finds the leftmost adjacent pair with the smallest sum, merges them, and increments the operation `count`. This process repeats until the array becomes non-decreasing or no more pairs can be merged.

1. **Check Non-Decreasing Condition**: For each iteration, the algorithm first checks if the array is non-decreasing by comparing each element with its next neighbor.

1. **Find Minimum Sum Pair**: If the array is not non-decreasing, it scans the array to find the leftmost adjacent pair with the smallest sum.

1. **Merge the Pair**: The identified pair is replaced with their sum, effectively merging them into a single element.

1. **Repeat**: The process repeats until the array becomes non-decreasing or no more merges are possible.

This approach ensures that the array is gradually transformed into a non-decreasing sequence with the minimum number of operations by always targeting the most critical pairs first (those with the smallest sums).

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n^2)`, where n is the length of the array.

- **Space Complexity**: `O(n)`, as the array is modified in place, but slicing operations may create new temporary arrays during the merge step.
