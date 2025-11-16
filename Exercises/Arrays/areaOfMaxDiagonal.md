# Maximum Area of Longest Diagonal Rectangle

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/).

## Initial Approach

The initial approach uses a straightforward iterative scan of the input list dimensions. It applies the Pythagorean theorem to calculate the diagonal length for each rectangle, which is $d = \sqrt{l^2 + w^2}$.

- If the `current_diagonal` is equal to `longest_diagonal`, the `max_area` is updated to be the maximum of its current value and the current rectangle's area. This ensures that in the case of a tie in diagonal length, the rectangle with the greatest area is selected.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
