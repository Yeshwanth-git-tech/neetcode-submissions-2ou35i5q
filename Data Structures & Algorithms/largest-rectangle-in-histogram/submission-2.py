class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxarea = 0

        for i , h in enumerate(heights):
            #i will ahve a startt index, so that they can move backwards
            start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                area = height * (i - index)
                maxarea = max(area , maxarea)
                start = index
            stack.append([start , h])

        
        for i , h in stack:
            area = h * (len(heights) - i)
            maxarea = max(area , maxarea)

        return maxarea






        