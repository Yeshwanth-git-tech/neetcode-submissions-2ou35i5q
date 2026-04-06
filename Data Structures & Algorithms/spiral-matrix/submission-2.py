class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # res = []
        # while matrix:
        #     res+= matrix.pop(0)

        #     if matrix:
        #         matrix = [list(row) for row in zip(*matrix)][::-1]
            
        # return res

        ##so above is recursive way using zip to match the index position piars and unpack and reverse 
        #First unpack , then zip and then reverse

        ##now intutive way 

        res = []

        while matrix:
            res+=matrix.pop(0)

            #[[4, 5,6][7,8,9]]
            if matrix and matrix[0]:
                for row in matrix:
                    #not matrix.pop()
                    res.append(row.pop())
            #[[4,5], [7,8]]

            if matrix:
                res+=matrix.pop()[::-1]

            ##remaining [[4,5]]
             # ↑ up
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res
                
