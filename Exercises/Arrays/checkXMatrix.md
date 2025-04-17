# Check if Matrix Is X-Matrix

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/).

## Initial Approach

The initial approach involves iterating through each element of the square matrix and checking whether it lies on one of the two diagonals (main diagonal or anti-diagonal).

1. **Diagonal Check**: For each element at position `(i, j)`, determine if it is part of either the main diagonal (`i == j`) or the anti-diagonal (`i + j == n - 1`, where `n` is the matrix size).

1. **Non-Zero Check**: If the element is on a diagonal, it must be non-zero; otherwise, it must be zero.

1. **Early Termination**: If any element violates these conditions, return `False` immediately. If all checks pass, return `True`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n^2)`, where n is the size of the matrix.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
