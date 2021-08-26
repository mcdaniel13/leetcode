from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        maxCharCnt = self.getMaxCharCnt(s)
        length = len(s)
        for charCnt in range(1, maxCharCnt + 1):
            startIdx = endIdx = curCharCnt = charCntLeastk = 0
            cntMap = [0] * 26
            while endIdx < length:
                if curCharCnt <= charCnt:
                    idx = ord(s[endIdx]) - ord('a')
                    if cntMap[idx] == 0:
                        curCharCnt += 1
                    cntMap[idx] += 1
                    if cntMap[idx] == k:
                        charCntLeastk += 1
                    endIdx += 1
                else:
                    idx = ord(s[startIdx]) - ord('a')
                    if cntMap[idx] == k:
                        charCntLeastk -= 1
                    cntMap[idx] -= 1
                    if cntMap[idx] == 0:
                        curCharCnt -= 1
                    startIdx += 1

                if curCharCnt == charCnt and curCharCnt == charCntLeastk:
                    res = max(res, endIdx - startIdx)

        return res

    def getMaxCharCnt(self, s) -> int:
        res = 0
        check = [False] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            if not check[idx]:
                res += 1
                check[idx] = True

        return res


sol = Solution()
print(sol.longestSubstring("ababacb", 3))
print(sol.longestSubstring("aaabb", 3))
print(sol.longestSubstring("ababbc", 2))
