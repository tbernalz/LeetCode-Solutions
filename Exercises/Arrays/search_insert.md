# Search Insert Position

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/search-insert-position/description/).

## Initial Approach

The way I solved this problem was by recognizing that the array is sorted, so I could use **binary search** instead of looping through every element. This makes things much faster. My goal was to either find the exact position of the target or figure out where it should go if it’s not already in the array.

I started with two pointers: `left` at the beginning of the array and `right` at the end. Then I kept calculating the middle position (`check_position`) to check if the target matched the value at that position.

If the target was smaller than the middle value, it meant I should focus on the left half, so I moved the `right` pointer closer to the middle. If the target was larger, I moved the `left` pointer to skip the left half and look at the right. I repeated this until the pointers narrowed down to where the target either was or where it should be inserted.

This approach makes sense because binary search is efficient for sorted arrays, and it guarantees the result in fewer steps compared to checking each element one by one. It felt logical to me to "cut the problem in half" at every step instead of brute-forcing it.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(log n)`, where n is the length of the array.

  - The binary search algorithm halves the search range with every iteration, resulting in logarithmic time complexity.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
