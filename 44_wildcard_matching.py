class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = "0" + s
        p = "0" + p
        dp = [[False] * (len(p)) for i in range(len(s))]
        dp[0][0] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue

                if (i > 0 and j > 0) and (s[i] == p[j] or p[j] == "?"):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i-1][j] | dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[len(s) - 1][len(p) - 1]

sol = Solution()
print(sol.isMatch("","?"))
# print(sol.isMatch("aa", "a"))
# print(sol.isMatch("aa", "*"))
# print(sol.isMatch("cb", "?a"))
# print(sol.isMatch("adceb", "*a*b"))
# print(sol.isMatch("acdcb", "a*c?b"))