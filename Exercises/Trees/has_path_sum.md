# Path Sum

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/path-sum/description/).

## Initial Approach

I realized that I needed to implement a `depth-first search (DFS)` traversal of the binary tree. It starts from the root node and recursively explores each root-to-leaf path, keeping track of the cumulative sum of node values along the path.

**For each node:**

1. The current sum is updated by adding the node's value.

1. If the node is a leaf (no left or right children), the current sum is compared to the `target_sum`. If they match, the function returns `True`.

1. If the node is not a leaf, the function recursively checks the left and right subtrees.

1. If any path matches the `target_sum`, the function returns `True`; otherwise, it returns `False`.

1. This approach ensures that all root-to-leaf paths are explored, and the correct result is returned based on whether any path sums to the `target_sum`.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of nodes in the binary tree.

- **Space Complexity**: `O(k)`, where k is the height of the tree.
