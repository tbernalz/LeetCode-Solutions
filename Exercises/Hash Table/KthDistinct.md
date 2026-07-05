# Majority Element

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/majority-element/description/).

## Initial Approach

The initial approach utilizes a frequency-tracking strategy using a dictionary. It begins by extracting the unique elements from the array to initialize a dictionary where each distinct string acts as a key with a starting count of zero.

The algorithm then performs a two-pass process:

1. First Pass: It iterates through the entire array to populate the dictionary, counting how many times each string appears.
2. Second Pass: It loops through the array a second time in its original order. For each string, it checks the dictionary to see if its frequency is exactly 1 (meaning it is distinct). A counter tracks how many distinct strings have been found so far; as soon as this counter matches `k`, that string is returned.

If the loop finishes and fewer than `k` distinct strings exist, it returns an empty string.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * m)`, where n is the number of strings in the array and m is the maximum length of a string, since we iterate through the array of n elements multiple times, and each dictionary operation (hashing and equality checking) requires processing the string character-by-character up to length m.
- **Space Complexity**: `O(n * m)`, where n is the number of strings in the array and m is the maximum length of a string, since the dictionary creation requires storing up to n unique keys, with each key consuming memory proportional to its string length m.
