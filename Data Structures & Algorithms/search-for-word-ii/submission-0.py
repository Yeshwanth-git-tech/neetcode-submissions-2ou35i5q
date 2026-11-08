class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        
        for w in words:
            d = trie
            for c in w:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d["$"] = w

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r , c , dd):
            if (r<0 or c<0 or r == rows or c== cols):
                return
            # board[r][c] = ch , 
            ch = board[r][c]
            if ch not in dd:
                return 
            #if forgot to move the pointer again
            dd = dd[ch]
            # if ch not in dd:
            #     return 
            if "$" in dd:
                res.append(dd["$"])
                #fiorgit to del
                del dd["$"]
            
            board[r][c] = "#"
            dfs(r+1 , c , dd)
            dfs(r-1 , c , dd)
            dfs(r , c+1 , dd)
            dfs(r , c-1 , dd)
            board[r][c] = ch
        
        for r in range(rows):
            for c in range(cols):
                dfs(r , c , trie)
        return res
            