# Find the Child Who Has the Ball After K Seconds

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/).

## Initial Approach

In my initial approach, I observed the cyclic pattern of the ball being passed back and forth among the children. To simulate this behavior efficiently, I used the following steps:

1. **Cycle Length**:

   I derived the formula `(n × 2) − 2` to calculate the total length of one complete cycle of the ball, where: - `n` is the number of children. - The ball moves forward to the last child and then back to the first child in a "zig-zag" motion.

1. **Modulo Operation**:

   Using modular arithmetic, I determined the position of the ball within this cycle after `k` seconds: `position = k % cycle length`.

1. **Adjusting for Overflow**:

   If the position exceeded the number of children (`n`), I adjusted it by subtracting the cycle length until the position fell within the valid range of `[0, n−1]`.

This approach avoided manually simulating the entire sequence for `k` seconds, allowing for efficient computation even with large inputs.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(1)`, since these operations are constant with respect to n and k.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
