# Element Appearing More Than 25% In Sorted Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/).

## Initial Approach

The initial approach leverages the fact that the array is sorted in non-decreasing order. Since the array is sorted, any element that appears more than 25% of the time must span at least one position where `arr[i] == arr[i + quarter]`, where `quarter = len(arr) // 4`.

We iterate through the array and check for the first occurrence where `arr[i]` equals `arr[i + quarter]`. Due to the sorted nature of the array, this guarantees that the element appears more than 25% of the time.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
