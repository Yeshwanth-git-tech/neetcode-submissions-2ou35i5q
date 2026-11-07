class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []

        for i in range(len(position)):
            pairs.append([position[i] , speed[i]])

        # print(pairs)

        # print(sorted(pairs)[::-1])
        #now decreasing montonic stack
        for p , s in sorted(pairs)[::-1]:
            stack.append( (target-p)/s )

            # print(stack)

            while len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
                    # we willnot pop the last car in the positon nearby to the target
                #as thats value will be a good one to check whether the other can pass it 

            
        return len(stack)