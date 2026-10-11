class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                # stack.append(int(stack.pop()) + int(stack.pop()))
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                #order matters
                a = stack.pop()
                b = stack.pop() #this is the first element added
                stack.append(b-a)
            elif c == "/":
                #order matters
                a = stack.pop()
                b = stack.pop() #this is the first element added
                #round to zero , integer division
                #stack.append(int(b)// int(a))
                stack.append(int(b/a))
            elif c == "*":
                # stack.append(int(stack.pop()) * int(stack.pop()))
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        return stack[0]