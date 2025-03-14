# Maximize the Total Height of Unique Towers

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/description/).

## Initial Approach

The initial approach involves sorting the `maximumHeight` array in descending order to prioritize assigning the highest possible heights to the towers. This ensures that we maximize the sum of the heights while maintaining the constraint that no two towers can have the same height.

The algorithm iterates through the sorted array and assigns the maximum possible height to each tower, ensuring that the assigned height is less than or equal to the maximum allowed height for that tower and also less than the height assigned to the previous tower (to avoid duplicates). If at any point it becomes impossible to assign a valid height (i.e., the assigned height drops below 1), the function returns `-1`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the `maximumHeight` array.

  - The `O(n log n)` comes from sorting the maximumHeight array.
  - The `O(n)` comes from iterating through the sorted array to assign heights.
  - Total time complexity: `O(n log n)` + `O(n)` = `O(n log n)`

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
