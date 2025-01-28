# Transformed Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/transformed-array/description/).

## Initial Approach

To solve the problem, I focused on building the `result` array by iterating through the input array `nums` and applying the transformation rules directly. For each element in `nums`:

- If the number is positive (`nums[i] > 0`), I moved `nums[i]` steps to the right, wrapping around to the start of the array using modular arithmetic.

- If the number is negative (`nums[i] < 0`), I moved `abs(nums[i])` steps to the left, ensuring the circular behavior by using the same modular operation.

- For zero (`nums[i] == 0`), I directly assigned the value to the corresponding position in the `result` array.

The key insight I used was leveraging modular arithmetic to handle the circular nature of the array efficiently. Instead of repeatedly adding or subtracting the array length, I simplified the calculations by using `(i + nums[i]) % len_nums`. This approach allowed me to maintain clarity and avoid unnecessary loops.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the `nums` array.
- **Space Complexity**: `O(n)`, where n is the length of the `result` array, which has the same length as the `nums` one.
