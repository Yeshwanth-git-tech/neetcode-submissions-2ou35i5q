class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d["$"] = "$"
        

    def search(self, word: str) -> bool:
        def dfs(i ,d):
            if i == len(word):
                return "$" in d
            

            c = word[i]
            if c == ".":
                for key in d:
                    # if key = "$":
                    #     continue
                    if key!="$" and dfs(i+1, d[key]):
                        return True
                    
                return False
            else:
                if c not in d:
                    return False
                return dfs(i+1 , d[c])
                #so it is the i , trie tree
        d = self.trie
        return dfs(0 , d)
        
