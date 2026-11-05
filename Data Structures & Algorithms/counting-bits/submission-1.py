class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            cnt = 0
            x = i
            while x:
                cnt+=x%2
                x = x>> 1
            res.append(cnt)    
        return res    