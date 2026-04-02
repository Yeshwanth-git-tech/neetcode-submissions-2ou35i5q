class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #so it pops temp and then index
                tempT , tempI = stack.pop()
                res[tempI] = (i - tempI)
            stack.append([t , i])
        return res