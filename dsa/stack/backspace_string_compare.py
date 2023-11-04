class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_final_string(string):
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    del stack[-1]
            return stack
        return get_final_string(s) == get_final_string(t)
