from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Determines if a binary tree has a root-to-leaf path where the sum of all it's nodes equals a given number.

        Args:
            root (Optional[TreeNode]): The binary tree to analyze.
            target_sum (int): The number to reach by summing the root-to-leaf paths.

        Returns:
            bool: True if there's a root-to-leaf path that sums to the target_sum, False otherwise.
        """

        def dfs(node: Optional[TreeNode], current_sum: int) -> bool:
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == target_sum

            return dfs(node.left, current_sum) or dfs(node.right, current_sum)

        return dfs(root, 0)
