# The Two Sneaky Numbers of Digitville

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/).

## Initial Approach

The initial approach leverages a hash set to efficiently detect duplicates in a single pass through the array. As the list `nums` is traversed, each number is checked for presence in the `seen` set. If a number is already present, it is identified as a duplicate and added to the `duplicated` list.

This process continues until exactly two duplicate numbers are found, at which point the loop breaks early to avoid unnecessary iterations. Using a hash set ensures constant-time lookups and efficient overall performance.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the lenght of the array.

- **Space Complexity**: `O(n)`, where n is the lenght of the array.
