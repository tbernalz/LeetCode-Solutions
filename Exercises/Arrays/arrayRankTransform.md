# Rank Transform of an Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/rank-transform-of-an-array/description/).

## Initial Approach

The initial approach involves sorting the array while keeping track of the original indices of each element. This allows us to assign ranks based on the sorted order while ensuring that elements with the same value receive the same rank.

1. **Index Tracking**: Create a list of tuples where each tuple contains an element from the array and its original index. This helps in placing the ranks back into their correct positions in the original array.

1. **Sorting**: Sort this list of tuples based on the element values. Sorting helps in determining the rank order since ranks are assigned based on the relative size of elements.

1. **Rank Assignment**: Iterate through the sorted list and assign ranks. If the current element is the same as the previous one, it receives the same rank. Otherwise, the rank is incremented.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * log n)`, where n is thelength of the array.

- **Space Complexity**: `O(n)`, where n is thelength of the array.
