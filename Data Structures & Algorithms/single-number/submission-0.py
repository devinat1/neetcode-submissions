from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = Counter()
        for num in nums:
            seen[num] += 1

        for k, v in seen.items():
            if v == 1:
                return k
        
