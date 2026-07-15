# Contains Duplicate

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/contains-duplicate/description/).

## Initial Approach

The initial approach uses a hash set to track elements as we iterate through the array.

Instead of comparing every element to every other element (which would be a brute-force $O(n^2)$ approach), we loop through the array once. For each number, we try to add it to our hash set. The Add() method in a set naturally returns false if the item is already present. By checking this return value immediately, we can detect a duplicate the very instant we encounter an element we've already seen, allowing for an early return.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.
- **Space Complexity**: `O(n)`, where n is the length of the array.
