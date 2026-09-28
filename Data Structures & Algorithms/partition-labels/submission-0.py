class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        end = 0

        lastindex = {}
        res = []

        for i , c in enumerate(s):
            lastindex[c] = i

        for i in range(len(s)):
            size+=1
            end = max(end , lastindex[s[i]])
            #we have reached the last index of that particular character
            if i == end:
                res.append(size)
                size = 0

        return res

        