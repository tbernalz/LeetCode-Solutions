# Minimum Time to Type Word Using Special Typewriter

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/).

## Initial Approach

I initially thought of mapping each letter to its position using a dictionary (abecedarium) and tracking the current position on the typewriter. The idea was straightforward: for each character in the word, calculate the clockwise and counter-clockwise distances and then add the smaller of the two distances to the total time, along with 1 second for pressing the key. After typing a letter, I updated the current position to reflect the newly typed character.

```Python
class Solution(object):
    def minTimeToType(self, word: str) -> int:
        """
        Calculate the minimum number of seconds to type a word on a circular typewriter.

        Args:
            word(str): The word to type.

        Returns:
            int: Minimum number of seconds to type the word.
        """
        abecedarium = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
            'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
            'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
            'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
        }
        seconds = 0
        current_char_position = 1

        for i in word:
            distance = abs(current_char_position - abecedarium[i])
            if distance > (len(abecedarium) / 2):
                distance = abs(distance - len(abecedarium))
            seconds += distance + 1
            current_char_position = abecedarium[i]

        return seconds

```

## Optimized Solution

After looking at other solutions and getting some help, I learned that I could simplify my approach significantly by using the ord() function to directly calculate distances based on ASCII values. This eliminated the need for a dictionary entirely. For each character in the word, I calculated both the clockwise and counter-clockwise distances and added the smaller one to the total time, along with 1 second for pressing the key. This made the code cleaner and more efficient.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n)`, where n is the length of the input word.
- **Space Complexity**: `O(1)`, as the dictionary is fixed and no additional space is used relative to the input size.

**Optimized Solution**:

- **Time Complexity**: `O(n)`, where n is the length of the input word.
- **Space Complexity**: `O(1)`, as no additional data structures are used.
