from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Removes all nodes with the given value from the linked list.

        Args:
            head (Optional[ListNode]): The head of the linked list.
            val (int): The value to be removed from the list.

        Returns:
            Optional[ListNode]: The head of the modified linked list.
        """
        previous_node = head
        new_head = None
        new_head_found = False

        while head:
            if head.val == val:
                previous_node.next = head.next
            else:
                previous_node = head
                if not new_head_found:
                    new_head_found = True
                    new_head = head

            head = head.next

        return new_head
