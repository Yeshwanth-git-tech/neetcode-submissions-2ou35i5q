class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxwater = 0
        while l<r:
            height = min(heights[l] , heights[r])
            breadth = r-l
            area = height * breadth
            maxwater = max(maxwater , area)

            if heights[l] < heights[r]:
                l+=1
            else:
                #this will take care >=
                r-=1   
        return maxwater