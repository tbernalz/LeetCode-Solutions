# Two Sum

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/two-sum/description/).

## Initial Approach

When approaching the problem, I recognized that a hash map could be used to store numbers and their indices as I iterated through the list. For each number, I calculated its complement (target - num) and checked if this complement existed in the hash map. If it did, I returned the indices of the current number and its complement. This approach ensures efficient lookups and avoids nested loops, making it faster `O(n)` than a brute-force method `O(n^2)`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of elements in the list.
- **Space Complexity**: `O(n)`, as the hash map stores up to n elements.
