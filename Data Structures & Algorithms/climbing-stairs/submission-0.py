class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}
        def r(x):
            if x in visited:
                return visited[x]
            if x == n:
                return 1
            if x > n:
                return 0

            visited[x] = r(x + 1) + r(x + 2)
            return visited[x]

        r(0)
        print(visited)
        return r(0)
