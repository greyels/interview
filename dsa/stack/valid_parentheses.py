class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['[', '(', '{']
        closed = [']', ')', '}']
        stack = []
        for char in s:
            if char in opened:
                stack.append(char)
            else:
                if len(stack) != 0 and stack[-1] == opened[closed.index(char)]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
