class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for letter in s[::-1]:
            if letter != " ":
                count += 1
            else:
                break
        return count

    def lengthOfLastWord2(self, s: str) -> int:
        s_list = s.strip().split(" ")
        return len(s_list[-1])

    def lengthOfLastWord3(self, s: str) -> int:
        if not s:
            return 0
        first_spaces = False
        count = 0
        if s[-1] == " ":
            first_spaces = True
        for i in s[::-1]:
            if i == " " and first_spaces:
                continue
            elif i == " " and not first_spaces:
                break
            else:
                count += 1
                first_spaces = False
        return count
