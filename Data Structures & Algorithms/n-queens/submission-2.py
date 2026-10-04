class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        #r+c
        posdiag = set()
        #r-c
        negdiag = set()


        board = [["."]*n for i in range(n)]

        res = []

        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):

                if c in cols or (r+c) in posdiag or (r-c) in negdiag or board[r][c] == "Q":
                    continue

                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res




