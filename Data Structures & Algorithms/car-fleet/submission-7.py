class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #target. =speed/posiotn is the stack
        # stack = []

        # for i in range(len(position)):
        #     stack.append( (target - position[i])/speed[i] )
        # #we ahev to dort the stack in reverse order 
        # stack = sorted(stack)[::-1]

      
        
        # for i in range(len(stack)-1 , -1 , -1):
        #     while len(stack)>1 and stack[-2]>=stack[-1]:
        #         stack.pop()
    

        # return len(stack)

        stack = []

        pairs = []

        for i in range(len(position)):
            # pairs.append([speed[i] , position[i]])
            #we ahve top sorit it with positon
            pairs.append([position[i] ,speed[i]] )
        

        for p , s in sorted(pairs)[::-1]:
            stack.append((target - p)/s)

            # while len(stack) > 1 and stack[-1] <= stack[-2]:
            while len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        
        