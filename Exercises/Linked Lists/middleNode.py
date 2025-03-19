from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a given singly linked list.

        Args:
            head (Optional[ListNode]): The head node of the given singly linked list.

        Returns:
            Optional[ListNode]: The middle node of the linked list. If the list has two middle nodes, the second one is returned.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
