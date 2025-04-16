# Shuffle an Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/shuffle-an-array/description/).

## Initial Approach

The initial approach involves using the **Fisher-Yates algorithm** to generate a uniformly random permutation of the array. The algorithm works by iterating through the array from the last element to the first. At each step, it selects a random index `j` between `0` and the current index `i` (inclusive) and swaps the elements at positions `i` and `j`. This ensures that every permutation of the array is equally likely.

The `reset()` method simply returns the original array, while the `shuffle()` method applies the Fisher-Yates algorithm to a copy of the original array to avoid modifying it directly.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(n)`, where n is the length of the array.
