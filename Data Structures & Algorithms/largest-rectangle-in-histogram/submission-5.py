class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                maxarea = max(maxarea , (i - index) * height)
                start = index
            stack.append([start , h])
      
        # print(stack)
        # for i , h in stack:
        #     print(i , h)


        for i , h in stack:
            maxarea = max(maxarea , (len(heights)-i) * h)
        return maxarea
        #     for istack):
        #         maxarea = max(maxaarea , (len(heights)-i)* h)
        # return maxarea