from collections import deque


class Solution:
    def validPath(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        """
        Check if there's a path between two nodes in an undirected graph.

        Args:
            n(int): The number of vertices.
            edges(list[list[int]]): The edges of the graph.
            source(int): The source node.
            destination(int): The destination node.

        Returns:
            bool: True if a path exists, False otherwise.
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False
