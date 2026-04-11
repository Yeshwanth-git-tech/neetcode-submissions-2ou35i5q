class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        ##O(m+n) space

        ROWS = len(matrix)
        COLS = len(matrix[0])
        # #first we find the zeros
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             rows.add(r)
        #             cols.add(c)

        # #now set rows and cols which are zero
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if r in rows or c in cols:
        #             matrix[r][c] = 0

        #this is easy m*n , now using O(1) constant space
        #so in this is we will have zero flag , for row 0
        #then first col and the inner matrix r > 0
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    #set the first col value to zero
                    #we are using the first col as marker
                    matrix[0][c] = 0
                    if r > 0:
                        #using the first row as marker
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        #now lets set zero in the inner matrix 

        for r in range(1 , ROWS):
            for c in range(1 , COLS):
                #this is awesome if the first col 00 , 01 , 02 or 10 , 20
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        #first col 00

        if matrix[0][0] == 0:
            #here , 00 , 01 , 02 and 00 , 10 , 11 , 12
            for r in range(ROWS):
                matrix[r][0] = 0

        #now the first row only that r = 0 , 00 , 10 , 20 and 01 , 02
        if rowZero:
            # for r in range(ROWS):#0 , 1 , 2 r will be always zero
            for c in range(COLS):# 0 ,1 2
                matrix[0][c] = 0




            

                   