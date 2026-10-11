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
                # Use int(b / a).

# The difference only shows up with negative numbers:

# Expression	7 and 2	-7 and 2
# int(b / a)	3	-3 ✅
# b // a	3	-4 ❌
# // rounds down, toward negative infinity, so -3.5 becomes -4
# int() rounds toward zero, so -3.5 becomes -3
# The problem asks for rounding toward zero, so use int(b / a)

# Easy way to remember:

# // means floor, and floor always goes down
# int() just cuts off the decimal part
                stack.append(int(b/a))
            elif c == "*":
                # stack.append(int(stack.pop()) * int(stack.pop()))
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        return stack[0]