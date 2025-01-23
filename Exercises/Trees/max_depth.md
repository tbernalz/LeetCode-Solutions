# Maximum Depth of Binary Tree

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/).

## Initial Approach

In my initial approach, I observed that the problem of finding the maximum depth of a binary tree can be broken down into recursive subproblems:

1. **Recursive Nature of the Problem**:

   - The depth of a binary tree is determined by the longer path between the left and right subtrees, plus one for the current node.
   - For each node, I recursively compute the maximum depth of its left and right children.

1. **Base Case**:

   - If the node is None, it signifies the absence of a subtree, so the depth at that point is 0.

1. **Recursive Step**:

   - I calculated the depth of the left and right subtrees using recursive calls.

This straightforward approach is based on the divide-and-conquer principle, where the problem is divided into smaller, similar problems at each node.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of nodes in the binary tree.

- **Space Complexity**: `O(k)`, where k is the height of the tree.
