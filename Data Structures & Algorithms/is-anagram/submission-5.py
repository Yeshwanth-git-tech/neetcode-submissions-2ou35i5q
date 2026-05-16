from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        hash1 = {}
        hash2 = {}

        for i in s:
            hash1[i] = hash1.get(i , 0) + 1
        for i in t:
            hash2[i] = hash2.get(i , 0) + 1
        
        return hash1 == hash2
        