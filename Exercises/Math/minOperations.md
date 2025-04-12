# Minimum Operations to Make Array Sum Divisible by K

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-`k`/description/).

## Initial Approach

The initial approach involves calculating the sum of all elements in the array and then determining the remainder when this sum is divided by `k`. The key observation here is that if the sum is already divisible by `k`, no operations are needed (remainder is 0). Otherwise, the remainder itself represents the minimum number of decrement operations required to make the sum divisible by `k`. This is because decrementing any element by the remainder amount will adjust the sum to be exactly divisible by `k`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
