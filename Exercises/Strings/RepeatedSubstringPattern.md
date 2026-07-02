# Repeated Substring Pattern

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/repeated-substring-pattern/description/)

## Initial Approach

The approach used in this solution is a substring simulation method. It works by iterating through all possible pattern lengths, starting from length 1 up to half the length of the string (since a repeated substring must repeat at least twice to form the original string).

For each potential length, it first checks if the total length of the string is divisible by this potential pattern length. If it is, it extracts the potential pattern from the beginning of the string (`s[0..i]`). It then iterates through the rest of the string in chunks of that same length, checking if every chunk matches the extracted pattern. If a full match is found across the entire string, it returns `true`. If no valid pattern satisfies this after checking all possible lengths, it returns `false`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * d)`, where nF is the length of the string and d is the number of divisors of n.
- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
