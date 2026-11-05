class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            x = i
            cnt = 0
            while x:
                cnt+=x%2
                # x = x//10
                x = x >> 1

            res.append(cnt)

        return res
        