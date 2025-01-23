# Last Visited Integers

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/last-visited-integers/description/).

## Initial Approach

The initial approach follows an iterative strategy that utilizes two arrays: `seen` and `ans`. The choice to use arrays and perform operations like `insert` and `append` was guided by the requirements of the exercise. If not restricted by these requirements, a more efficient data structure like a deque or stack could have been used for managing the `seen` elements.

The algorithm processes the input array nums element by element:

1. When a positive integer is encountered, it is inserted at the front of the `seen` array using the `insert(0, num)` method. This ensures that the most recent positive integers are tracked at the beginning of the array.

1. When a `-1` is encountered, the algorithm counts how many consecutive -1s have been `seen` so far (`k`). If `k` is less than the length of `seen`, the `k`-th most recently added positive integer is appended to `ans`. Otherwise, `-1` is appended to handle cases where there are insufficient preceding positive integers.

This approach ensures the output array `ans` is constructed as required by the problem.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n^2)`, where n is the length of the array nums.

  - The O(n^2) complexity comes from the use of the `insert(0, num)` operation on the seen array, which takes `O(n)` in the worst case due to element shifting. Since this operation is performed for each element in `nums`.

- **Space Complexity**: `O(n)`, as the `seen` array may store up to all positive integers encountered in `nums`, and the `ans` array stores the result.
