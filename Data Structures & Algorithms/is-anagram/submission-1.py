from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap1 = {}
        # hashmap2 = {}

        # for c in s:
        #     hashmap1[c] = hashmap1.get(c , 0) + 1
        
        # for c in t:
        #     hashmap2[c] = hashmap2.get(c, 0) + 1

        # return hashmap1 == hashmap2

        print(Counter(s))
        print(Counter(t))
        return Counter(s) == Counter(t)