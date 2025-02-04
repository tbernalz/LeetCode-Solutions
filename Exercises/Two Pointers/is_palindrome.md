# Valid Palindrome

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/valid-palindrome/description/).

## Initial Approach

First, I cleaned up the string by removing all non-alphanumeric characters and converting everything to lowercase. This gave me a filtered version of the string that I could directly compare with its reverse to check if it was a palindrome.

This method is super simple and makes good use of Python’s built-in string operations. But while it works, it’s not the most efficient since it creates a whole new string just for comparison.

```Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a phrase is a palindrome.

        Args:
            s(str): The phrase to analyze.

        Returns:
            bool: True if the phrase is a palindrome, False otherwise.
        """
        formatted_string = "".join(char.lower() for char in s if char.isalnum())

        return formatted_string == formatted_string[::-1]


```

## Optimized Solution

After looking into better ways to do this, I realized a two-pointer approach is way more efficient. Instead of building a new string, I can just scan from both ends at the same time, skipping over non-alphanumeric characters as needed. If the characters at the `left` and `right` pointers don’t match, it’s immediately not a palindrome. Otherwise, I keep moving the pointers inward until they meet or cross.

This method cuts down on memory usage since I’m working with the original string directly—no extra space needed! Plus, it’s just a cleaner and faster way to solve the problem.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n),`, where n is the length of the input string.
- **Space Complexity**: `O(n)`, where n is the length of the input string.
  - The space is used to store the `formatted_string`, which can be as large as the input string.

**Optimized Solution**:

- **Time Complexity**: `O(n),`, where n is the length of the input string.

* **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
