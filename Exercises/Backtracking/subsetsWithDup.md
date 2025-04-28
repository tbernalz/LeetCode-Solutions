# Subsets II

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/subsets-ii/description/).

## Initial Approach

The initial approach involves generating all possible subsets of the given array while avoiding duplicate subsets. Since the array may contain duplicates, sorting the array first ensures that duplicates are adjacent, making it easier to skip them during subset generation.

The solution uses a backtracking strategy where:

1. The array is sorted to handle duplicates efficiently.

1. A helper function (`backtrack`) is used to explore all possible subsets:

   - It starts by adding the current subset to the `result`.

   - For each subsequent element, it checks if the current element is a duplicate of the previous one (and not the first occurrence in the current recursion level). If so, it skips to avoid duplicate subsets.

   - Otherwise, it includes the element, recursively continues building the subset, and then backtracks by removing the element to explore other possibilities.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * 2^n)`, where n is the length of the array.

  - Sorting takes `O(n log n)`, but the dominant part is the subset generation.

  - There are `2^n` possible subsets (since each element can either be included or excluded).

  - For each subset, we perform an `O(n)` operation to copy the current subset into the result list.

  - Thus, the total time complexity is `O(n * 2^n)`.

- **Space Complexity**: `O(n * 2^n)`,

  - The space required to store all subsets is `O(2^n)`, and each subset can be up to `O(n)` in size.

  - The recursion stack uses `O(n)` space (depth of recursion tree).
