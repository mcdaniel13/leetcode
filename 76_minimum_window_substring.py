from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        tCounter = Counter(t)
        sCounter = Counter()
        charCnt = len(tCounter.keys())
        matchCnt = 0

        ans = ""

        start = 0
        end = 0
        while start < len(s):
            if matchCnt < charCnt:
                if end == len(s):
                    return ans

                sCounter[s[end]] += 1
                if 0 < tCounter[s[end]] == sCounter[s[end]]:
                    matchCnt += 1
                end += 1
            else:
                sCounter[s[start]] -= 1
                if 0 < tCounter[s[start]] == sCounter[s[start]] + 1:
                    matchCnt -= 1
                start += 1

            if matchCnt == charCnt:
                if not ans or end - start < len(ans):
                    ans = s[start:end]

        return ans



sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("a", "a"))
print(sol.minWindow("a", "aa"))