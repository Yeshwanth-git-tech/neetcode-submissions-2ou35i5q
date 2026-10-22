class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjlist = {c:[] for w in words for c in w}

        print(adjlist)

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            minlen = min(len(word1) , len(word2))

            if len(word1) > len(word2) and  word1[:minlen] == word2[:minlen]:
                return ""

            for j in range(minlen):
                if word1[j]!=word2[j]:
                    adjlist[word1[j]].append(word2[j])
                    break
        print(adjlist)
        path = set()
        visited = set()
        res = []
        def dfs(char):
            if char in path:
                return False

            if char in visited:
                return True

            path.add(char)

            for nei in adjlist[char]:
                if not dfs(nei):
                    return False


            path.remove(char)
            visited.add(char)
            res.append(char)

            return True


        for c in adjlist:
            if not dfs(c):
                return ""

        return "".join(res[::-1])