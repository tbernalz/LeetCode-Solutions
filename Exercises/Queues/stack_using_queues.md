# Implement Stack using Queues

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/implement-stack-using-queues/description/).

## Initial Approach

The initial approach involves using two queues to simulate the behavior of a stack. The key idea is to maintain the order of elements such that the last pushed element is always at the front of the primary queue (`q1`), allowing for LIFO operations.

- **Push Operation**:

  - The new element is added to the secondary queue (`q2`).

  - All elements from the primary queue (`q1`) are moved to `q2`, ensuring the new element is at the front.

  - The queues are then swapped, so `q1` now contains all elements with the most recent addition at the front.

- **Pop Operation**:

  - Simply remove and return the front element from `q1`, which is the most recently pushed element (top of the stack).

- **Top Operation**:

  - Return the front element of `q1` without removing it.

- **Empty Operation**:

  - Check if `q1` is empty.

This approach ensures that all stack operations adhere to the LIFO principle using only standard queue operations.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**:

  - **Push Operation**: `O(n)`, where n is the number of elements in the stack.

  - **Pop Operation**: `O(1)`.

  - **Top Operation**: `O(1)`.

  - **Empty Operation**: `O(1)`.

- **Space Complexity**: `O(n)`, where n is the number of elements in the stack.
