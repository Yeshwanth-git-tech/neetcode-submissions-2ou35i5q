class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1

        top = 0
        bot = len(matrix)-1

        while top<=bot:
            m = (top+bot)//2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        if not(top<=bot):
            return False

        row = (top+bot)//2
    
        while l<=r:
            m = (l+r)//2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False

        