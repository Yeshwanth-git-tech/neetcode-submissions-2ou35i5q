class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #better to always gave a list
        res = []
        

        minlen = min(len(word1) , len(word2))
        for i in range(minlen):
            res.append(word1[i])
            res.append(word2[i])

        #so remaining
        if minlen == len(word1):
            res.append(word2[minlen:])
        else:
            res.append(word1[minlen:])
        return "".join(res)