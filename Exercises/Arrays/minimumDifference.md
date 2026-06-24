# Minimum Difference Between Highest and Lowest of K Scores

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/).

## Initial Approach

The initial approach to solving this problem efficiently relies on the insight that to minimize the difference between the highest and lowest of any `k` values, the chosen ones should be as close to each other as possible.

To make that happen, we sort the array first. Sorting perfectly groups neighboring numbers together. Once sorted, any consecutive group of `k` numbers is a candidate. We then slide a fixed-size window of length `k` across the array, checking the gap between the first element (the lowest) and the last element (the highest) of that window to grab the absolute minimum difference.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n log n)`, where n is the length of the array.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
