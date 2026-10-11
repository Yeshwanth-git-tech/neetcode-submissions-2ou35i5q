class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])

        stack = []
        for p , s in sorted(pairs)[::-1]:
            #first we append the time taking for the car to reach the target
            stack.append( (target - p) / s)
            #so the car beghind can reach before the car in front 
            #then its a fleet so stack[-2] is the car with max positon
            while len(stack) >=2 and stack[-1] <= stack[-2]:
                #will pop stack[-1] #basically we are merging
                stack.pop()

        return len(stack)
         
           




        
        