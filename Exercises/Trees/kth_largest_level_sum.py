from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        Calculate the k-th largest level sum in a binary tree. The level sum is the sum of the values of all nodes on the same level.

        Args:
            root(Optional[TreeNode]): The root node of the binary tree.
            k(int): The k-th largest level sum to find (1-based index).

        Returns:
            int: The k-th largest level sum. If the tree has fewer than k levels, returns -1.
        """
        level_sum = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sum.append(current_level_sum)

        if len(level_sum) < k:
            return -1

        level_sum.sort(reverse=True)
        return level_sum[k - 1]
