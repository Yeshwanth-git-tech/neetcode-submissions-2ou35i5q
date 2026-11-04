class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowzero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    #then top row depict the cols that needs to be set zero
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowzero = True

        for r in range(1 , rows):
            for c in range(1 , cols):
                #row =1 , col =0 so this the marked row
                #row = 0 , col = c shifting so first row expect the fftisrt cel , 
                if matrix[r][0] == 0 or matrix[0][c]==0:
                    matrix[r][c] = 0
        
        for r in range(rows):
            if matrix[0][0] == 0:
                #first col needs to be set zero all vals
                matrix[r][0] = 0

        for c in range(cols):
            if rowzero:
                matrix[0][c] = 0
        