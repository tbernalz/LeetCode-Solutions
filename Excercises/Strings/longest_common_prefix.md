# Longest Common Prefix

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/longest-common-prefix/description/).

## Initial Approach

The initial approach is not brute force but rather an iterative refinement strategy. It starts by assuming the first string in the list is the longest common prefix and then iteratively compares it with the remaining strings in the array.

For each string, the `startswith()` method is used to check if the current prefix matches. If a mismatch is found, the prefix is shortened character by character (using slicing) until it matches the current string or becomes empty. This continues for all strings, ensuring the longest common prefix is gradually narrowed down.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * k)`, where `n` is the lenght of the array and `k` is the length of the longest common prefix or the first string

  - The O(n) comes from the loop iterating through all the `strs` words.
  - The O(k) is due to for each string, the startswith() operation compares characters in the prefix, which can take O(k) in the worst case. Thus, the total time complexity is `O(n * k)`.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
