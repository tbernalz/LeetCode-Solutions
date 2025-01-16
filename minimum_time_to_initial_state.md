# Minimum Time to Revert Word to Initial State I

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/description/).

## Initial Approach

```python
import math


class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        """
        Calculates the minimum time to revert a word with some operations.

        Args:
            word(str): The word to process.
            k(int): The number of characters to remove and add from the word.

        Returns:
            int: The minimum time required for the word to revert to its initial state.
        """
        word_length = len(word)
        fragment_count = 1
        comparison_start = 0
        current_start = k

        while current_start < word_length:
            comparison_fragment = word[comparison_start : comparison_start + k]
            current_fragment = word[current_start : current_start + k]
            comparison_fragment = comparison_fragment[: len(current_fragment)]

            if comparison_fragment == current_fragment:
                if current_start + k >= word_length:
                    return fragment_count
                comparison_start += k
                current_start += k
            else:
                fragment_count += 1
                comparison_start = 0
                current_start = fragment_count * k

        return math.ceil(word_length / k)

```

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**:
- **Space Complexity**:
