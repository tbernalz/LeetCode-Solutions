# Removing Minimum and Maximum From Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/).

## Initial Approach

The initial approach involves identifying the positions of the minimum and maximum elements in the array. Once these positions are known, we calculate the number of deletions required to remove both elements by considering three possible scenarios:

1. **Option 1**: Remove all elements from the start of the array up to and including the maximum element.

1. **Option 2**: Remove all elements from the minimum element to the end of the array.

1. **Option 3**: Remove elements from the start up to and including the minimum element, and also remove elements from the maximum element to the end of the array.

The minimum number of deletions is then determined by taking the smallest value among these three options.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
