class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        nei = defaultdict(list)

        wordList.append(beginWord)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] +"*" + w[j+1:]
                nei[pattern].append(w)

        q = deque([beginWord])
        visit = set()
        visit.add(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                w=q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res+=1
    
        res = 0
        return res
