# Longest Uncommon Subsequence I

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/longest-uncommon-subsequence-i/description/).

## Initial Approach

(The easiest exercise in LeetCode so far, hahaha)

The approach is straightforward and avoids unnecessary complexity. Since the problem is to find the longest uncommon subsequence (**LUS**) between two strings `a` and `b`, the solution is based on a simple observation:

- If the two strings are identical (`a == b`), there can be no uncommon subsequence, so the result is `-1`.

- Otherwise, the longest uncommon subsequence would be the longer of the two strings, as the entirety of one string is guaranteed to not be a subsequence of the other.

This approach bypasses brute force methods of generating and comparing subsequences, opting instead for a direct comparison and length evaluation.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(1)`, The algorithm performs a constant number of operations (equality check and length comparisons), regardless of the input size.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
