class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0


        if beginWord in words:
            words.remove(beginWord)

        q = deque()
        q.append((beginWord , 1))

        m = len(beginWord)

        lowercase = "abcdefghijklmnopqrstuvwxyz"

        while q:
            w , n = q.popleft()
            if w == endWord:
                return n
            for i in range(m):
                for c in lowercase:
                    if c == w[i]:
                        continue
                    new_word = w[:i] + c + w[i+1:]
                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word , n+1))
        return 0
                

           