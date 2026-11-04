class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # l = 0
        # r = len(matrix)-1

        # while l<r:
        #     # for i in range(l , r):
        #     for i in range(r - l):
        #         top = l
        #         bot = r
        #         topleft = matrix[top][l+i]

        #         matrix[top][l+i] = matrix[bot-i][l]
        #         # bottomleft = matrix[bot][l]

        #         # bottomright = matrix[bot][r]
        #         matrix[bot-i][l] = matrix[bot][r-i]

        #         # topright = matrix[top][r]
        #         matrix[bot][r-i] =  matrix[top+i][r]

        #         #now swap top right
        #         # matrix[top+i][r] = matrix[top][l+i]
        #         matrix[top+i][r] = topleft

        #     r-=1
        #     l+=1


        for r in range(len(matrix)):
            for c in range(r+1 , len(matrix)):
                matrix[r][c] , matrix[c][r] = matrix[c][r] , matrix[r][c]


        # for r in range(len(matrix)):
        #     matrix[r].reverse()

        n = len(matrix)
        for r in range(n):
            for c in range(n // 2):
                matrix[r][c] , matrix[r][n-c-1] = matrix[r][n-c-1] , matrix[r][c] 

        