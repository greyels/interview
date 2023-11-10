# Cамая длинная подстрока s, содержащая не более k различных символов
def longest_k_substring(s: str, k: int) -> int:
    if not s or k < 1:
        return -1
    if len(s) == 1:
        return 1
    slow, fast = 0, 1
    seen, max_len = dict(), 1
    seen[s[slow]] = 1
    while fast < len(s):
        seen[s[fast]] = seen.get(s[fast], 0) + 1
        while len(seen) > k:
            seen[s[slow]] -= 1
            if seen[s[slow]] == 0:
                del seen[s[slow]]
            slow += 1
        max_len = max(max_len, fast - slow + 1)
        fast += 1
    return max_len


assert (longest_k_substring("eceba", 2)) == 3
assert (longest_k_substring("eceeeba", 2)) == 5
assert (longest_k_substring("eccceba", 1)) == 3
assert (longest_k_substring("eccceba", 0)) == -1
assert (longest_k_substring("", 1)) == -1
assert (longest_k_substring("a", 1)) == 1
print("OK")
