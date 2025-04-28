# Uncommon Words from Two Sentences

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/uncommon-words-from-two-sentences/description/).

## Initial Approach

The initial approach involves combining both sentences into a single string and then splitting this combined string into individual words. We then count the occurrences of each word using a dictionary.

For each word in the combined list, we check if it appears exactly once. If it does, we consider it an uncommon word and include it in our result list. This approach leverages the fact that an uncommon word must appear exactly once across both sentences and not appear in the other sentence.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n + m)`, where n is the length of `s1` and m is the length of `s2`.

- **Space Complexity**: `O(n + m)`, where n is the length of `s1` and m is the length of `s2`.
