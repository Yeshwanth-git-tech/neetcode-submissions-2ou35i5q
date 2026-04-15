class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #here basically the l >= r , if l < r skip . 

        l = 0
        r = len(heights)-1
        maxarea = 0
        while l < r:
            width = r - l 
            curr_area = min(heights[l], heights[r])*width
            maxarea = max(curr_area , maxarea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1            
        return maxarea