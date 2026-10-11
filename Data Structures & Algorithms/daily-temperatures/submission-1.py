class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #index , temp
        #im assignning 0 as if we doint find a valid temperature then we return 0
        res = [0]*len(temperatures)
        for i , t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                tempindex , temp = stack.pop()
                res[tempindex] = i - tempindex
            stack.append([i , t])

        return res



        