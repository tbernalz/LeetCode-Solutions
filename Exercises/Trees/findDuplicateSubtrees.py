from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        """
        Finds and returns all duplicate subtrees in a binary tree.

        A duplicate subtree is defined as a subtree that has the same structure and node values as another subtree in the tree.
        For each type of duplicate subtree, only one root node of any of the duplicates is returned.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[Optional[TreeNode]]: A list of root nodes of all duplicate subtrees. Each duplicate subtree is represented by one of its root nodes.
        """
        subtree_map = defaultdict(int)
        result = []

        def dfs(node: Optional[TreeNode]) -> tuple:
            if not node:
                return None

            subtree = (node.val, dfs(node.left), dfs(node.right))
            if subtree_map[subtree] == 1:
                result.append(node)

            subtree_map[subtree] += 1

            return subtree

        dfs(root)
        return result
