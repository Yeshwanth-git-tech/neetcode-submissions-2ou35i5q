class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # adj = defaultdict(list)

        adj = {c:[] for w in words for c in w}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1] if i+1<len(words) else None

            minlen = min(len(word1) , len(word2))

            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""

            for j in range(minlen):
                if word1[j]!=word2[j]:
                    adj[word1[j]].append(word2[j])
                    break
        
        visited = set()
        path = set()
        res = []
        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True
            path.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            path.remove(c)
            visited.add(c)
            res.append(c)
            return True


        for c in adj:
            if not dfs(c):
                return ""
        return "".join(res[::-1])                