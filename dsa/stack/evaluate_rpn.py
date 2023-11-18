from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operations = ("+", "-", "*", "/")
        for token in tokens:
            if token in operations:
                last = stack.pop()
                prev = stack.pop()
                if token == "+":
                    stack.append(prev + last)
                elif token == "-":
                    stack.append(prev - last)
                elif token == "*":
                    stack.append(prev * last)
                elif token == "/":
                    stack.append(int(prev / last))
            else:
                stack.append(int(token))
        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
assert Solution().evalRPN(tokens) == 22
print("OK")
