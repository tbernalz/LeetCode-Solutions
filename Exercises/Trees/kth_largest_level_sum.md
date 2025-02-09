# Kth Largest Sum in a Binary Tree

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/).

## Initial Approach

The initial approach focuses on level-order traversal using a queue to calculate the sum of node values at each level of the binary tree. By using a **breadth-first search (BFS)** technique, the algorithm ensures that all levels are processed in sequence. During traversal, the sum of values for each level is computed and stored in a list. Once all level sums are gathered, the list is sorted in descending order to identify the k-th largest sum. If the number of levels is less than `k`, the algorithm returns -1.

This approach avoids unnecessary computations by processing the tree level by level and sorting only after all sums are collected.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of nodes in the binary tree.

- **Space Complexity**: `O(w + l)`, where w is the maximum width of the tree and l the length of the array that stores the sum of values for each level.
