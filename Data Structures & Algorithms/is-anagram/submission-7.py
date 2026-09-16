# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # c1 = Counter(s)
        # c2 = Counter(t)

        # return c1 == c2

        h1 = {}

        h2 = {}

        for letters in s:
            h1[letters] = h1.get(letters , 0) + 1

        for letters in t:
            h2[letters] = h2.get(letters ,0) + 1

        return h1 == h2