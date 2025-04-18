# Single Element in a Sorted Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/single-element-in-a-sorted-array/description/).

## Initial Approach

The initial approach involves using **binary search** to efficiently locate the single non-duplicate element in the sorted array. The key observation is that in a sorted array where every other element appears exactly twice, the single element disrupts the pattern of pairs.

By checking the middle element and its adjacent elements, we can determine whether the single element lies to the `left` or `right` of the current midpoint. Adjusting the search range based on this comparison allows us to narrow down the possible location of the single element in logarithmic time.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(log n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
