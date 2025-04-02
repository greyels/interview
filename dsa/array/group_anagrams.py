from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in hash:
                hash[sorted_str] = [string]
            else:
                hash[sorted_str].append(string)
        return [value for value in hash.values()]

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            hash[sorted_str].append(string)
        return list(hash.values())
