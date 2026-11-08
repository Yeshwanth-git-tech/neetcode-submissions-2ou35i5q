class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        orderin = {c:i for i , c in enumerate(s)}


        size = 0
        end = 0

        res = []

        for i in range(len(s)):
            end = max(end , orderin[s[i]])
            size+=1
            if i == end:
                res.append(size)
                size = 0

        return res