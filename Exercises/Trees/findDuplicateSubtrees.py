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
