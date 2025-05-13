# Alternating Digit Sum

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/alternating-digit-sum/description/).

## Initial Approach

The initial approach involves converting the given integer `n` into a string to easily iterate over each digit. The most significant digit (leftmost) is assigned a positive sign, and the sign alternates for each subsequent digit.

For each digit in the string representation of `n`, the approach checks its position (index). If the index is even, the digit is added to the result; if the index is odd, the digit is subtracted from the result. This ensures the correct alternate digit sum is computed.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(k)`, where k is the number of digits on n.

- **Space Complexity**: `O(k)`, where k is the number of digits on n.
  - The additional space is used to store the string `n_str`, which has k characters.
