# Number of Changing Keys

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/number-of-changing-keys/description/).

## Initial Approach

The initial approach is an iterative strategy where the string is traversed character by character, starting from the second character. It maintains a `current_key` variable to track the last "key" being used (case-insensitively).

For each character in the string, it checks if the lowercase version of the current character differs from `current_key`. If so, it increments the count of key changes (`key_changes`) and updates `current_key` to the lowercase version of the current character. This ensures that the solution dynamically tracks transitions between keys while ignoring case differences.

This approach avoids the overhead of nested loops and handles case-insensitivity directly during the comparison, ensuring simplicity and efficiency.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the input string s.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
