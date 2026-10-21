class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1

        while top<bot:
            m = (top+bot)//2

            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break

        if top > bot:
            return False


        targetrow = (top+bot)//2

        l = 0
        r = len(matrix[0])-1

        while l<=r:
            m = (l+r)//2
            if target > matrix[targetrow][m]:
                l = m+1
            elif target < matrix[targetrow][m]:
                r = m-1
            else:
                return True
        return False
