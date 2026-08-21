from collections import defaultdict

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(int)

        def r(floor):
            if floor >= len(cost):
                return 0
            if floor in dp:
                return dp[floor]
            
            dp[floor] = cost[floor] + min(r(floor + 1), r(floor + 2))
            return dp[floor]
        
        return min(r(0), r(1))

        # cost[step] = OPT(cost[step + 1], cost[step + 2])