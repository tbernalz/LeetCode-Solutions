# Middle of the Linked List

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/middle-of-the-linked-list/description/).

## Initial Approach

The initial approach is a straightforward method to find the middle node of a singly linked list. It involves two traversals of the linked list:

- **First Traversal**: The length of the linked list is calculated by iterating through all nodes until the end is reached. This is done using a `while` loop that increments a counter (`linked_list_len`) for each node visited.

- **Second Traversal**: Once the length of the list is known, the middle node is found by traversing the list again up to the middle index (`linked_list_len // 2`). This is done using a `for` loop.

While this approach works correctly, it is not the most efficient because it requires traversing the list twice. However, it is easy to understand and implement.

```Python
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_len = 1
        current_head = head

        while True:
            current_head = current_head.next
            if current_head:
                linked_list_len += 1
            else:
                break

        current_head = head

        for _ in range(linked_list_len // 2):
            current_head = current_head.next

        return current_head

```

## Optimized Solution

The optimized solution uses the **Two-Pointer Technique (Tortoise and Hare)**. This approach involves only a single traversal of the linked list:

1. **Two Pointers**: A `slow` pointer moves one step at a time, while a `fast` pointer moves two steps at a time.

1. **Termination**: When the `fast` pointer reaches the end of the list (either `fast` is `None` or `fast.next` is `None`), the `slow` pointer will be at the middle node.

1. **Return**: The `slow` pointer, which now points to the middle node, is returned.

This approach is more efficient because it only requires one traversal of the list, reducing the number of operations compared to the initial approach.

## Complexity

**Initial Approach**:

- **Time Complexity**: `O(n)`, where n is the number of nodes in the linked list.

  - The first traversal to calculate the length takes `O(n)`.

  - The second traversal to find the middle node takes `O(n/2)`.

  - Combined, the time complexity is `O(n)`.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.

**Optimized Solution**:

- **Time Complexity**: `O(n)`, where n is the number of nodes in the linked list.

  - The two-pointer technique traverses the list only once, with the `fast` pointer moving twice as `fast` as the `slow` pointer.

  - This results in `O(n/2)` operations, which simplifies to `O(n)`.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
