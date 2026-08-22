class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # l = 0 
        maxwater = 0
        # for r in range(1 , len(heights)):
        #     if heights[r] > heights[l]:
        #         l=r
        #         r+=1
        #     width = r - l
        #     height = min(heights[l], heights[r])
        #     print(width , height)
        #     curr = width * height
        #     maxwater = max(maxwater , curr)
        #     # print(maxwater)
        # return maxwater

        #but this above solutiondeos not take into consideration of width , max width and hight can also be an optimal solution
        l = 0
        r = len(heights)-1
        while l < r:
            width = (r - l)
            height = min(heights[l] ,heights[r])
            currarea = width * height

            maxwater = max(maxwater , currarea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

            ## so if both the heights are equal the above else takes care of it as 
            #if heights[r] > heights[l]:
            #r-=1 , and if both heights are equal then decrement r or increement l , so that comes to above else condition


        return maxwater
        
            
