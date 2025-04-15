# Permutations

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/permutations/description/).

## Initial Approach

The initial approach uses a **backtracking algorithm** to generate all permutations of the given array of distinct integers. The idea is to build permutations incrementally by selecting one element at a time from the remaining elements and then backtracking to explore other possibilities.

- **Backtracking Function**: The `backtrack` function takes a `path` (current permutation being built) and `remaining` (elements not yet used in the permutation). If no elements are left, the current permutation is added to the result.

- **Recursive Exploration**: For each element in `remaining`, it is added to `path`, and the function is called recursively with the updated path and the remaining elements (excluding the current one). After the recursive call, the element is removed from `path` (backtracking step) to allow other permutations to be explored.

```Python
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible unique permutations of an array of distinct integers.

        Args:
            nums (List[int]): An array of distinct integers for which permutations are to be generated.

        Returns:
            List[List[int]]: All the possible permutations.
        """

        def backtrack(path: List[int], remaining: List[int]) -> None:
            if not remaining:
                result.append(path.copy())
                return

            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i + 1 :])
                path.pop()

        result = []
        backtrack([], nums)

        return result

```

## Optimized Solution

The optimized solution also uses backtracking but reduces the overhead of list slicing by swapping elements in place. This avoids creating new sublists during each recursive call, improving efficiency.

- **In-Place Swapping**: Instead of slicing `remaining`, the current element is swapped with the first element of `remaining`. The recursive call is then made with the sublist starting from the next element (`remaining[1:]`).

- **Restoration**: After the recursive call, the elements are swapped back to their original positions to maintain the integrity of the array for subsequent iterations.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n * n!)`, where n is the length of the array.

  - There are `n!` permutations, and for each permutation, we perform `O(n)` operations (due to the loop and recursive calls).

- **Space Complexity**: `O(n * n!)`, where n is the length of the array.

  - `n!` is from the number of permutations (since there are `n!` possible orderings of `n` distinct elements).

  - `n` is from the size of each permutation (since every permutation is an array of length `n`).

**Optimized Solution**:

- **Time Complexity**: `O(n * n!)`, where n is the length of the array.

  - There are `n!` permutations, and for each permutation, we perform `O(n)` operations (due to the loop and recursive calls).

- **Space Complexity**: `O(n * n!)`, where n is the length of the array.

  - `n!` is from the number of permutations (since there are `n!` possible orderings of `n` distinct elements).

  - `n` is from the size of each permutation (since every permutation is an array of length `n`).
