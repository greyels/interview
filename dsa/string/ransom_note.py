class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for char in magazine:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        for char in ransomNote:
            if char in letters:
                letters[char] -= 1
                if letters[char] < 0:
                    return False
            else:
                return False
        return True


magazine = "abbreviation"
ransomNote = "reviation"
assert Solution().canConstruct(ransomNote, magazine), True
print("OK")
