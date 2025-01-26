# Make Three Strings Equal

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/make-three-strings-equal/description/).

## Initial Approach

I focused on finding the longest common prefix among the three strings since that part determines how much of each string can remain after deletions. Starting with the shortest string length as the limit, I compared characters at each position across all three strings. If the characters matched, I extended the common prefix; otherwise, I stopped. If no common prefix existed, I returned `-1` because the strings couldn’t be made equal. Finally, I calculated the number of deletions for each string as the difference between its length and the common prefix length and summed them.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the length of the shortest string among s1, s2, and s3.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
