from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # make adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for v in adj[node]:
                dfs(v)

        # go through each node in n
            # DFS it and add the other nodes to visited
            # return the length of visited
        res = 0
        for u in range(n):
            if u not in visited:
                res += 1
                dfs(u)
            
        return res
        