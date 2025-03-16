# Find Peak Element

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/find-peak-element/description/).

## Initial Approach

The initial approach uses a **binary search** strategy to efficiently find a peak element in the array. The algorithm works by maintaining two pointers, `left` and `right`, which represent the current search range. At each step, the middle element (`mid`) is compared with its neighbors to determine if it is a peak. If not, the search range is narrowed to the side where a higher value exists, as a peak must lie in that direction. This process continues until the search range is reduced to two elements, and the higher one is returned as the peak.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(logn)`, where n is the length of the array.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
