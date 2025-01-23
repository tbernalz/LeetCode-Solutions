# Count the Number of Consistent Strings

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/count-the-number-of-consistent-strings/description/).

## Initial Approach

To solve this problem, I used a set to store the "allowed" characters for a few reasons:

- Why Not Keep the "allowed" String? While we could check membership directly in the string, it would take O(k) time per character (where k is the length of the "allowed" string). Converting the string to a set ensures O(1) membership checks, significantly improving performance.
- Fast Lookups: A set is perfect for checking if a character exists because it has an average O(1) lookup time. This is way faster than using a list (O(n)) and has the same complexity as a dictionary O(1).
- Unique Characters: If the "allowed" string has duplicates, converting it to a set removes them automatically. This keeps the solution clean and avoids unnecessary checks.
- Why Not a Dictionary? A dictionary also has O(1) lookups, but it stores key-value pairs. Since we only care about the keys (characters), a set is simpler, more appropriate, and uses less memory.

Once I have the "allowed" characters in a set, I iterate through each word in the words list. For each word, I use Python's all() function to check if all the characters in the word are in the set. If they are, I increment my counter for consistent strings.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(k + n * m)`, where k is the length of the "allowed" string, n the number of words in the words list and m be the average length of a word in words.

  - The `O(k)` comes from converting "allowed" to a Set
  - The `O(n * m)` is due to iterating over each of the n words, where the all() function checks all m characters of a word against the set.

- **Space Complexity**: `O(k)`, where k is the number of unique characters in the "allowed" string.
