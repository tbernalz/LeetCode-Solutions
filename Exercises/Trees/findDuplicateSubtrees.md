# Find Duplicate Subtrees

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/find-duplicate-subtrees/description/).

## Initial Approach

The initial approach involves using a **depth-first search (DFS)** traversal to serialize each subtree in the binary tree. The serialization is done by representing each subtree as a tuple containing the node's value and the serialized representations of its left and right subtrees. This serialized tuple is then used as a key in a dictionary (`subtree_map`) to track the frequency of each subtree.

As the DFS traverses the tree, it checks if the serialized subtree has been seen before. If a subtree appears exactly once before, it is added to the result list as a duplicate. This ensures that only one root node of each duplicate subtree type is included in the result.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of nodes in the binary tree.
- **Space Complexity**: `O(n)`, where n is the number of nodes in the binary tree.
