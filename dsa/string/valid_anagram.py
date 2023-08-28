class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = dict()
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        for char in t:
            if char in hash_map and hash_map[char] != 0:
                hash_map[char] = - 1
            else:
                return False
        return True


s = "aacc"
t = "ccac"
assert Solution().isAnagram(s, t), False
print("OK")
