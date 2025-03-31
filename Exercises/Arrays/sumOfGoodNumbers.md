# Sum of Good Numbers

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/sum-of-good-numbers/description/).

## Initial Approach

The solution iterates through each element in the array and checks if it is strictly greater than its left neighbor at index `i - k` and right neighbor at index `i + k` (if those indices exist). If both conditions are satisfied (or neighbors don’t exist), the element is considered "good," and its value is added to the total sum.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the `nums` array
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
