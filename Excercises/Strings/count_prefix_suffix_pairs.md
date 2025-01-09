# Count Prefix and Suffix Pairs I

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/).

## Initial Approach

As soon as I saw the problem, I recognized that I should use a brute-force approach to check all possible combinations of prefix and suffix pairs in the list of words. The idea was to iterate through all pairs of indices `(i, j)` where `i < j` and determine if the word at index `i` is both a prefix and a suffix of the word at index `j`. That's where the helper function isPrefixAndSuffix appears.

This brute-force approach ensures that all possible valid pairs are evaluated, but I also noted that the nested loops might be computationally expensive for large inputs.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n^2 * k)`, where n is the number of words in the words list, and k is the average length of the words.

  - The O(n^2) comes from the nested loops iterating through all pairs of words.
  - The O(k) is due to the slicing and comparisons in the isPrefixAndSuffix function.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
