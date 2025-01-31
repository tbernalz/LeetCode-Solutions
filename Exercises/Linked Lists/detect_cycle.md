# Linked List Cycle II

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/linked-list-cycle-ii/description/).

## Initial Approach

I used **Floyd's Tortoise and Hare algorithm** which is an efficient way to detect cycles in a linked list. The algorithm uses two pointers, `slow` and `fast`, that traverse the list at different speeds.

- The `slow` pointer moves **one step** at a time.

- The `fast` pointer moves **two steps** at a time.

If there is a cycle, the `fast` pointer will eventually meet the slow pointer inside the cycle. Once a cycle is detected, the algorithm resets the slow pointer to the head of the list and moves both pointers **one step** at a time until they meet again. The meeting point is the start of the cycle.

This approach avoids using additional data structures (like a hash set) and works in constant space.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of nodes in the linked list.

  - n the worst case, the slow and fast pointers will traverse the list twice:

    1. Once to detect the cycle (if it exists).

    1. Once to find the start of the cycle.

- **Space Complexity**: `O(1)`, as no additional data structures are used, and all operations are performed in-place.
