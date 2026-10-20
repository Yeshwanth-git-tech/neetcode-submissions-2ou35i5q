class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []

        for i in range(len(position)):
            pairs.append([position[i] , speed[i]])
  
        stack = []

    
        for p , s in sorted(pairs)[::-1]:

            stack.append((target - p)/s)



            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

     
           




        
        