# Minimum Time to Revert Word to Initial State I

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/description/).

## Initial Approach

In my first solution, I simulated the operations step by step to track when the string reverted to its initial state. My process worked like this:

1. **Divide the string into fragments of size** `k` and compare these fragments sequentially:

    - `comparison_fragment` starts from the first `k` characters of the string.
    - `current_start` moves through subsequent fragments of size `k`.

1. **For each step**:

    - I compared `comparison_fragment` with `current_start`.
    - If they matched, I moved to the next pair of fragments.
    - If they didn’t match, I restarted the comparison with `comparison_fragment` set to the first fragment and `current_start` incremented by `k`.

1. **Edge Case**:

    - If the remaining characters in `current_start` were fewer than `k`, I truncated `comparison_fragment` to match the length of `current_start`.

1. The process continued until all fragments matched sequentially, indicating the string had reverted to its initial state. I returned the total number of iterations (`fragment_count`) required.

1. **Fallback**

    - If the string doesn't revert to its initial state within the simulated comparisons, I calculated the fallback as the number of fragments that the word has with `math.ceil(len(word) / k)`. This represents the worst-case scenario, ensuring the function always produces a result.

The key point was to use a **fragment-by-fragment comparison**, resetting the comparison when a mismatch occurred.

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

- **Time Complexity**: `O(n)`, where n is the length of the string "word".

    - The `O(n)` comes from the while loop, which processes the string in chunks of size k, iterating a maximum of `ceil(n / k)` times.
    - Each iteration involves slicing and comparing fragments of size `k`, both of which take `O(k)`, 
    - So `O(n / k) * O(k) = O(n)`.

- **Space Complexity**: `O(k)`, where `k` is the chunk size.
    - This comes from the slicing operations (comparison_fragment and current_fragment), which temporarily hold up to `k` characters in memory. No additional data structures are used.
