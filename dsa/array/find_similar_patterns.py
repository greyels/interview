from typing import List


# Given a list of words and a word, return the list of words that has similar patterns as given word.
# Ex: Words=[aabbcc, aakkff, akkffkk, tjjiijj, deftg]. word="mnnssnn".
# Output=[akkffkk, tjjiijj]
def find_similar_patterns(words: List[str], pattern: str) -> List[str]:
    def has_pattern(word):
        if len(word) != len(pattern):
            return False
        for i in range(len(word) - 1):
            slow, fast = i, i + 1
            if (word[slow] != word[fast] and pattern[slow] == pattern[fast]) \
                    or (word[slow] == word[fast] and pattern[slow] != pattern[fast]):
                return False
        return True

    return [word for word in words if has_pattern(word)]


# Ensure only matching patterns are returned
assert find_similar_patterns(["aabbcc", "aakkff", "akkffkk", "tjjiijj", "deftg"], "mnnssnn") == ["akkffkk", "tjjiijj"]

# Edge Cases
assert find_similar_patterns(["abcd", "bcda", "xyz", "mnop"], "efgh") == ["abcd", "bcda", "mnop"]  # Different letters, same pattern
assert find_similar_patterns(["a", "b", "c"], "d") == ["a", "b", "c"]  # Single-letter words should match
assert find_similar_patterns([], "xyz") == []  # Empty list should return empty result
assert find_similar_patterns([], "") == []  # Empty list and pattern should return empty result
assert find_similar_patterns(["adasd"], "") == []  # Empty pattern should return empty result
assert find_similar_patterns(["aaaa", "bbbb", "fff", "cccc"], "dddd") == ["aaaa", "bbbb", "cccc"]  # Same-character words match
print("All tests passed! ✅")
