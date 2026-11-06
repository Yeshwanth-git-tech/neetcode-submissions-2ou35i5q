class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        n = len(board)


        for r in range(n):
            for c in range(n):
                if board[r][c] ==".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3 , c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3 , c//3)].add(board[r][c])
        return True
