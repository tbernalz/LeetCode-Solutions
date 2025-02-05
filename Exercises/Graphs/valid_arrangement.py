from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
        """
        Given a 0-indexed 2D integer array `pairs` where each `pairs[i] = [start_i, end_i]`,
        this function returns any valid arrangement of pairs such that for every index `i`
        where `1 <= i < len(pairs)`, the condition `end_{i-1} == start_i` holds.

        Args:
            pairs (list[list[int]]): The list of pairs representing directed edges.

        Returns:
            list[list[int]]: A valid sequence of pairs satisfying the given condition.
        """
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break

        path = []
        stack = [start_node]

        while stack:
            node = stack[-1]
            if graph[node]:
                stack.append(graph[node].pop())
            else:
                last = stack.pop()
                if stack:
                    path.append((stack[-1], last))

        return path[::-1]
