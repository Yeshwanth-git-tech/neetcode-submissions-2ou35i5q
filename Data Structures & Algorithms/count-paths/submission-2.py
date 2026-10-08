class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row= [1]*n


        for i in range(m-1):
            #this is the row im going to change for each iteration

            newrow = [1]*n

            for j in range(n-2 , -1 , -1):
                #for m=3 , n=4 , we first fill , m = 2 , n= 3 cell
                newrow[j] = newrow[j+1] + row[j]

            row = newrow

        return row[0]

