from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0

        for j in range(len(prices)):
            while i < j and prices[j] < prices[i]:
                i += 1

            res = max(res, prices[j] - prices[i])
            j += 1

        return res
