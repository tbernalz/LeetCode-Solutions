# Check if a String Is an Acronym of Words

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/).

## Initial Approach

The approach is simple and keeps things efficient. Since the goal is to check if a string is an acronym of a list of words, the best way to do this is by taking the first letter of each word and forming a new string.

- If this newly formed string matches the given acronym, we return `True`.

- Otherwise, we return `False`.

Instead of manually looping and building the acronym step by step, we use a generator expression inside `"".join()`, making the solution both clean and optimized.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the array.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
