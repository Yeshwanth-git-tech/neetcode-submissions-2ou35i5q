class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r , c , preval):
            if (r<0 or r == rows or c<0 or c == cols or matrix[r][c] <=preval):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]

            res = 1

            res = max(res , 1 + dfs(r+1 , c , matrix[r][c]))
            res = max(res , 1 + dfs(r-1 , c , matrix[r][c]))
            res = max(res , 1 + dfs(r , c+1 , matrix[r][c]))
            res = max(res , 1 + dfs(r , c-1 , matrix[r][c]))

            dp[(r,c)] = res
            #dont forget to return res
            return res

        for r in range(rows):
            for c in range(cols):
                dfs(r,c, -1)

        return max(dp.values())




        