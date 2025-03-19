# Find the Peaks

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/find-the-peaks/description/).

## Initial Approach

The initial approach is an iterative strategy that checks each element in the array (except the first and last) to determine if it is a peak. A peak is defined as an element that is strictly greater than its immediate neighbors (left and right).

The algorithm iterates through the array from the second element to the second-to-last element. For each element, it compares the current element with its left and right neighbors. If the current element is greater than both neighbors, it is identified as a peak, and its index is added to the result list.

This approach ensures that all peaks are identified in a single pass through the array, making it efficient and straightforward.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the mountain array.
- **Space Complexity**: `O(m)`, where m is the number of peaks in the array.
