# Valid Arrangement of Pairs

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/valid-arrangement-of-pairs/description/).

## Initial Approach

When I first looked at this problem, I realized that it’s about **arranging directed pairs** so that the **end of one pair matches the start of the next**. This immediately made me think of **Eulerian paths in a directed graph**, which can be efficiently solved using **Hierholzer’s Algorithm**.

1. **Building the Graph**:

   - I treated each `[start, end]` pair as a **directed edge** and built an **adjacency list** (`graph`).

   - To determine the correct starting node, I tracked the **in-degree** and **out-degree** for each node.

   - If a node had `out-degree - in-degree == 1`, that meant it had an extra outgoing edge, making it the `Eulerian path start`. Otherwise, I used any node with
     outgoing edges.

2. **Applying Hierholzer’s Algorithm (Stack-Based DFS + Backtracking)**:

   - I used **Hierholzer’s Algorithm**, which is designed to find an **Eulerian path** (a path that visits every edge exactly once).

   - Using a **stack-based DFS**, I **traversed edges dynamically**, always moving to a connected node while removing used edges.

   - When a node had no more outgoing edges, I **backtracked** by popping nodes off the stack and storing them in `path`.

3. **Constructing the Result**:

   - Since backtracking records the path in reverse, I reversed it at the end to get the correct order.

   - The result is a list of pairs where `end[i-1] == start[i]`, forming a valid sequence.

By using **Hierholzer’s Algorithm**, this approach efficiently finds a valid arrangement without brute force, ensuring that every edge is used exactly once while keeping the traversal structured.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(n)`, where n is the number of pairs.

  - **Graph Construction**: Creating the adjacency list and tracking in/out degrees takes `O(n)` since we process each pair once.
  - **DFS Traversal (Hierholzer’s Algorithm)**: Every edge is visited and removed exactly once, leading to `O(n)` time.
  - **Reversing the Path**: Since the Eulerian path is stored in reverse order during traversal, reversing it at the end takes `O(n)`.

  Thus, the total time complexity is `O(n) + O(n) + O(n) = O(n)`.

- **Space Complexity**: `O(n)`, where n is the number of pairs.
