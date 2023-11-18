class Solution:
    def invertWords(self, s: str) -> str:
        stack = []
        res = ""
        for char in s:
            if char != " ":
                stack.append(char)
                continue
            for i in range(len(stack)):
                res += stack.pop()
            res += char
        return res + ''.join(stack[::-1])


string = "Hallo World"
assert Solution().invertWords(string) == "ollaH dlroW"
print("OK")
