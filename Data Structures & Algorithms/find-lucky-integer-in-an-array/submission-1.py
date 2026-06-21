from collections import defaultdict

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for num in arr:
            d[num] += 1
        
        gl = -1
        for num, count in d.items():
            if num == count and num > gl:
                gl = num
        
        return gl
        