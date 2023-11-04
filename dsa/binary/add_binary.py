class Solution:
    def addBinary(self, a: str, b: str) -> str:
        adx, bdx = len(a) - 1, len(b) - 1
        result = []
        remain = 0
        while adx >= 0 or bdx >= 0:
            if adx >= 0:
                cur_a = int(a[adx])
                adx -= 1
            else:
                cur_a = 0
            if bdx >= 0:
                cur_b = int(b[bdx])
                bdx -= 1
            else:
                cur_b = 0
            cur = cur_a + cur_b + remain
            remain = 0
            if cur == 2:
                cur = 0
                remain = 1
            elif cur == 3:
                cur = 1
                remain = 1
            result.append(cur)
        if remain != 0:
            result.append(remain)
        return ''.join(str(x) for x in result[::-1])


assert Solution().addBinary("11", "1") == "100"
print("OK")
