class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(wordList)
        if endWord not in words:
            return 0

        q = deque([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:j] + ch + word[j+1:]
                        if nxt in words:
                            words.remove(nxt)  # acts as visited
                            q.append(nxt)
            res += 1

        return 0
        