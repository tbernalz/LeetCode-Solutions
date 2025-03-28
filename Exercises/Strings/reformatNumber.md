# Reformat Phone Number

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/reformat-phone-number/description/).

## Initial Approach

The approach involves cleaning the input string by removing all spaces and dashes, then systematically grouping the digits into blocks of 3 until fewer than 4 digits remain. The remaining digits are formatted according to specific rules:

- If 4 digits remain, split them into two blocks of 2.

- If 3 digits remain, keep them as a single block.

- If 2 digits remain, keep them as a single block.

The algorithm iterates through the cleaned string, appending 3-digit blocks until the remaining digits are 4 or fewer. Then, it handles the final grouping and joins all blocks with dashes.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the input string.
- **Space Complexity**: `O(n)`, where n is the length of the input string.
