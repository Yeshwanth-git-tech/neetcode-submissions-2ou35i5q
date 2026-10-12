class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        maxarea = 0
        while l<r:
            height = min(heights[l], heights[r])
            breadth = r - l
            curr_area = height*breadth
            maxarea = max(curr_area , maxarea)

            #now shifting the pointers
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxarea
