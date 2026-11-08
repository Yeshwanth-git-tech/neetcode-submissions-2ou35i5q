class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #so bacialy. posdiag , bnegdiag , row , cols

        #so lets build the board

        # board = [[]*n for i in range(n)]
        board = [["."]*n for i in range(n)]
        posdiag = set()
        #r+c
        negdiag = set()
        #r-c

        cols = set()
        res = []

        def dfs(r):
            if r == n:
                # res.append("".join(row) for row in board)
                res.append(["".join(row) for row in board])
                return 
            #so basicaly r+c 

            for c in range(n):
                if (c in cols or (r+c) in posdiag or (r-c) in negdiag):
                    continue
                
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                # board[r][c] == "Q"
                board[r][c] = "Q"
                dfs(r+1)
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                # board[r][c] == "."
                board[r][c] = "."

        dfs(0)
        return res