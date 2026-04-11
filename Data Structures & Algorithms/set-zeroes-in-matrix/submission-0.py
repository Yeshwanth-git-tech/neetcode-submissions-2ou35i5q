class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        ##O(m+n) space
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        #first we find the zeros
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        #now set rows and cols which are zero
        for r in range(ROWS):
            for c in range(COLS):
                if r in rows or c in cols:
                    matrix[r][c] = 0

                   