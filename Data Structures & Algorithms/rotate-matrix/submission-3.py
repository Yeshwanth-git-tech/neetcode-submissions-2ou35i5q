class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #LeetCode uses the original reference
        #cant give new box , that is like just matrix = []
        #here we are using the same referece matrix[:] - matrix.copy()
        matrix[:] = [list(row)for row in zip(*matrix[::-1])]

        ##intiutive way

        # n = len(matrix)

        # for i in range(n):
        #     for j in range(i+1 , n):
        #         matrix[i][j]  , matrix[j][i] = matrix[j][i] , matrix[i][j]

        # for row in matrix:
        #     row.reverse()

        
        