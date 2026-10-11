class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #index , height  
        Maxarea = 0

        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                Maxarea = max(Maxarea , height *(i - index))
                start = index
            #if we dont find height lesser than previous height
            stack.append([start , h])

        for i , h in stack:
            Maxarea = max(Maxarea , h *(len(heights) - i))
        return Maxarea


        