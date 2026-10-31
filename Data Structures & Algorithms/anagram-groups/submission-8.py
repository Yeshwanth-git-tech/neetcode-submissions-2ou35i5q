class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        
        for s in strs:
            count = [0 for i in range(26)]
            for w in s:
                count[ord(w) - ord("a")]+=1
            #again i forgot hashmap lkey must be immutable
            key = tuple(count)
            hashmap[key].append(s)

        
        return list(hashmap.values())