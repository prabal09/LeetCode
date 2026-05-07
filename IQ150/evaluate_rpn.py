from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for t in tokens:
            if t == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif t == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif t == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif t == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(a/b))
            else:
                stack.append(int(t))
            # print(stack[-1])
        return stack[0]
