# Maximum Number of Pairs in Array

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/).

## Initial Approach

The initial approach uses a sorting-based strategy to group identical numbers together. By sorting the array first, any duplicate elements become adjacent, allowing us to find pairs linearly.

The algorithm iterates through the sorted array using a loop. It checks if the current element matches the next one. If a match is found, it increments the pair count and skips the next element to avoid reusing it. If they do not match, the current element is counted as a leftover. A final boundary check ensures that if the last element is left stranded without a partner, it is correctly counted as a leftover.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n log n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
