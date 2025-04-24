# Minimum Deletions to Make String Balanced

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/).

## Initial Approach

The initial approach involves iterating through the string while keeping track of the number of 'b's encountered. The goal is to ensure that no 'a' comes after a 'b'. For each 'a' encountered, we have two choices:

1. Delete the 'a' (incrementing the deletion count).

1. Delete all previous 'b's (using the count of 'b's tracked so far).

The solution dynamically chooses the minimum between these two options at each step, ensuring the least number of deletions required to balance the string.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the lenght of the string.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
