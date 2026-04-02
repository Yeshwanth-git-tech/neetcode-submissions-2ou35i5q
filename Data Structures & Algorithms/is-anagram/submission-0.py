class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap1 = {}
        hashmap2 = {}

        if len(s)!= len(t):
            return False
        for ch in s:
            hashmap1[ch] = hashmap1.get(ch, 0) + 1
        for ch in t:
            hashmap2[ch] = hashmap2.get(ch, 0) + 1

        return hashmap1 == hashmap2

    