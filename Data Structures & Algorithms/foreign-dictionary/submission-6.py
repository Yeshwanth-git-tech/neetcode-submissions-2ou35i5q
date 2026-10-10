class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        print(adj)
        
        #len(words) - 1 as we will compare the w , w+i
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            minlen  = min(len(w1) , len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""

            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        print(adj)

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
                    return ""

            path.remove(c)
            visited.add(c)
            res.append(c)
            return True

        
        # for w in words:
        #     for c in w:
        #         if not dfs(c):
        #             return ""
        for c in adj:
            if not dfs(c):
                return ""
        # print(res)

        return "".join(res[::-1])

        