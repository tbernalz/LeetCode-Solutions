# Subsets

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/subsets/description/).

## Initial Approach

The initial approach involves using **backtracking** to generate all possible subsets of the given array. The idea is to explore every possible combination by recursively building subsets, starting from an empty subset and gradually adding elements from the array.

- Start with an empty subset.

- For each element in the array, make a choice: either include the element in the current subset or exclude it.

- Recursively build subsets by considering each element one by one, ensuring no duplicates are generated since the input elements are unique.

- The recursion ensures all combinations are explored, and each valid subset is added to the result list.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n * 2^n)`, where n is the length of the array.

  - There are `2^n` possible subsets (since each element can either be included or excluded).

  - For each subset, we perform an `O(n)` operation to copy the current subset into the result list.

  - Thus, the total time complexity is `O(n * 2^n)`.

- **Space Complexity**: `O(n * 2^n)`,

  - The space required to store all subsets is `O(2^n)`, and each subset can be up to `O(n)` in size.

  - The recursion stack uses `O(n)` space (depth of recursion tree).
