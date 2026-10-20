class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)

        square = defaultdict(set)

        row = len(board)
        col = len(board[0])
    
        for r in range(row):
            for c in range(col):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in square[(r//3 , c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3 , c//3)].add(board[r][c])

        return True

#         Yes. The loop always runs exactly 81 times no matter what the board looks like, so it’s constant, O(1).

# Big O only grows when the input size can grow. A fixed size means O(1).