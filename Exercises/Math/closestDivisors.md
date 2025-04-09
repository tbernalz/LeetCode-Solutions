# Closest Divisors

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/closest-divisors/description/).

## Initial Approach

The initial approach involves finding the closest pair of divisors for both `num + 1` and `num + 2` and then selecting the pair with the smallest absolute difference.

1. **Finding Divisors**: For each candidate number (`num + 1` and `num + 2`), iterate from 2 up to the square root of the number to find all divisor pairs.

1. **Tracking Closest Pair**: For each divisor pair (`i, n // i`), check if their absolute difference is smaller than the current closest pair. Update the closest pair if a better candidate is found.

1. **Comparison**: After evaluating both candidates (`num + 1` and `num + 2`), return the pair with the smallest absolute difference.

This approach ensures that we efficiently find the closest divisors without brute-forcing all possible pairs.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(√n)`, where n is the value of `num + 2` (the larger of the two candidates).

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
