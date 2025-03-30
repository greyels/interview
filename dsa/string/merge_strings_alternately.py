# https://leetcode.com/problems/merge-strings-alternately
class Solution:
    def mergeAlternately1(self, word1: str, word2: str) -> str:
        import itertools
        return ''.join((''.join(list) for list in itertools.zip_longest(word1, word2, fillvalue='')))

    def mergeAlternately2(self, word1: str, word2: str) -> str:
        res = []
        max_len = len(word1) if len(word1) > len(word2) else len(word2)
        for i in range(max_len):
            try:
                res.append(word1[i])
            except:
                pass
            try:
                res.append(word2[i])
            except:
                pass
        return ''.join(res)

    def mergeAlternately3(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)

    def mergeAlternately4(self, word1: str, word2: str) -> str:
        res = []
        min_len = len(word1) if len(word1) < len(word2) else len(word2)
        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])
        if len(word1) < len(word2):
            res.extend(word2[i+1::])
        else:
            res.extend(word1[i+1::])
        return ''.join(res)
