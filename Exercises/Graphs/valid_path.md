# Find if Path Exists in Graph

For more details, see the [LeetCode Problem Description](https://leetcode.com/problems/find-if-path-exists-in-graph/description/).

## Initial Approach

I used **Breadth-First Search (BFS)** to determine if there is a valid path between the `source` and `destination` nodes in an undirected graph. The algorithm starts by building an adjacency list to represent the graph, where each vertex stores its neighboring vertices.

The BFS traversal begins from the `source` node, exploring all its neighbors level by level. A queue is used to manage the order of exploration, and a `visited` set keeps track of the nodes that have already been processed to avoid revisiting them. If the `destination` node is encountered during the traversal, the algorithm returns `True`. If the queue is exhausted without finding the `destination`, the algorithm returns `False`.

This approach ensures that the shortest path (in terms of the number of edges) is found if one exists, but in this problem, we only care about the existence of a path, not its length.

## Optimized Solution

Not available yet.

## Complexity

- **Time Complexity**: `O(v + e)`, where v is the number of vertices (nodes) in the graph and e is the number of edges in the graph.

  - The O(v) comes from initializing the adjacency list and the visited set, as each vertex is processed once.

  - The O(e) comes from traversing all the edges in the graph during the BFS traversal. Each edge is processed once when exploring the neighbors of each vertex.

  Thus, the total time complexity is `O(v) + O(e) = O(v + e)`.

- **Space Complexity**: `O(v + e)`, where v is the number of vertices (nodes) in the graph and e is the number of edges in the graph.

  - The adjacency list requires O(v + e) space to store all vertices and their edges.
