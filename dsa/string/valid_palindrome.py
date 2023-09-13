class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_chars = [char.lower() for char in s if char.isalnum()]
        s = ''.join(alphanumeric_chars)

        if len(s) <= 1:
            return True
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


s = "A man, a plan, a canal: Panama"
assert Solution().isPalindrome(s) is True
print("OK")
