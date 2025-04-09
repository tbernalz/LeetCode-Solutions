# 3Sum

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/3sum/description/).

## Initial Approach

The initial approach involves sorting the array first to facilitate the **two-pointer technique**. The algorithm iterates through each element in the array, treating it as the first element of a potential triplet. For each element, it then uses two pointers (`left` and `right`) to find the other two elements that sum up to zero with the current element.

To avoid duplicates, the algorithm skips over repeated elements both for the outer loop (`i`) and the inner two-pointer traversal (`left` and `right`). This ensures that only unique triplets are added to the result.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n^2)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
