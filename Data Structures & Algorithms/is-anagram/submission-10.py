from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##brute force

        ##base condition 

        if len(s)!= len(t):
            return False
        # print(sorted(s))
        # # sorted(s) O(nlogn)
        # #comparing sorted(s) == sorted(t) O(n) O(nlogn) + O(n) 
        # #brute force time complexity is O(nlogn)
        # return sorted(s) == sorted(t)

        hashmap_s = {}
        hashmap_t = {}

        # for l in s:
        #     hashmap_s[l] = hashmap_s.get(l , 0) + 1

        # for l in t:
        #     hashmap_t[l] = hashmap_t.get(l , 0) + 1

        # return hashmap_s == hashmap_t 

        #using counter data structure same linear time and same space complexity O(n) + O(n) = O(n)

        return Counter(s) == Counter(t)


        

        


