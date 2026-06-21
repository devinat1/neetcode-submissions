from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for v in adj[node]:
                if v != parent:
                    if dfs(v, node) == False:
                        return False
            
            return True

        return dfs(0, None) and len(visited) == n
