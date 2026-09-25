class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digited = ''
        for digit in digits:
            digited += str(digit)
        
        digited = int(digited) + 1

        res = []
        for c in str(digited):
            res.append(int(c))
        return res
