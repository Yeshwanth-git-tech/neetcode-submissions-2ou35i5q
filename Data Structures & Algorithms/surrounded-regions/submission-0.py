class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows =len(board)
        cols = len(board[0])

        #i want to capture the O which cannot be converted tot X , theat is in all 4 borders

        def dfs(r , c):
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O"):
                return

            board[r][c] = "T" 
            dfs(r+1 , c)
            dfs(r-1 , c)
            dfs(r , c+1)
            dfs(r , c-1)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0,rows-1] or c in [0 ,cols-1]):
                    dfs(r , c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #now convert the capture T back to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        