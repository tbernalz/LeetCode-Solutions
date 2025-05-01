# Check if Array is Good

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/check-if-array-is-good/description/).

## Initial Approach

The initial approach involves verifying if the given array `nums` is a permutation of the `base[n]` array, where `base[n]` is defined as `[1, 2, ..., n-1, n, n]`. The steps are as follows:

1. **Determine `n`**: The length of `base[n]` is `n + 1`, so n is derived as `len(nums) - 1`.

1. **Check Edge Case**: If `n` is `0`, the array cannot be good since `base[0]` would be invalid (length 1, but `base[0]` is undefined).

1. **Sort and Compare**: Sort the input array and compare it with the expected `base[n]` array, which is constructed as `[1, 2, ..., n-1, n, n]`.

This approach leverages sorting to easily compare the input array with the expected `base[n]` pattern.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * log n)`, where n is the length of the array.

- **Space Complexity**: `O(n)`, where n is the length of the array.
