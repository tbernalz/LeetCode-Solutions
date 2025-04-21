# Split a String Into the Max Number of Unique Substrings

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/).

## Initial Approach

The initial approach is a **backtracking** strategy that explores all possible ways to split the string into unique substrings. It starts from the beginning of the string and iteratively tries to split the string into substrings of varying lengths, ensuring each `substring` is unique.

- For each possible split point, it checks if the current `substring` is not already in the set of `seen` substrings.

- If the `substring` is unique, it adds it to the set and recursively processes the remaining part of the string.

- After exploring all possibilities from that split point, it backtracks by removing the `substring` from the set to try other potential splits.

This approach ensures that all possible splits are considered, and the maximum number of unique substrings is tracked.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * 2^n)`, where n is the length of the string.

  - `O(2^n)` comes from the number of possible unique partitions of a string (each position has two choices: split or not split).
  - `O(n)` comes from slicing substrings and inserting/removing from the set.

- **Space Complexity**: `O(n^2)`, where n is the length of the string.

  - Up to `O(n)` substrings in the `seen` set
  - Plus, the recursive stack can go as deep as `O(n)`.
