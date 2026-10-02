class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        #r+c
        postdiag = set()
        #r-c
        negdiag = set()

        board = [["."]*n for i in range(n)]

        res = []

        def backtrack(r):
            if r == n:
                ans = ["".join(row) for row in board]
                res.append(ans)
                return

            for c in range(n):
                if c in cols or (r+c) in postdiag or (r-c) in negdiag:
                    continue

                cols.add(c)
                postdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                postdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)

        return res


