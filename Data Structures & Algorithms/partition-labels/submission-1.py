class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        end = 0

        orderindex = {c:i for i , c in enumerate(s)}

        print(orderindex)
        res = []
        for i in range(len(s)):
            end = max(end , orderindex[s[i]])
            size+=1
            if i == end:
                res.append(size)
                size = 0
                

        return res