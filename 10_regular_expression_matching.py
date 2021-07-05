class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[0][0] = True
        for i in range(len(p)):
            if p[i] == "*":
                dp[0][i + 1] = dp[0][i - 1]

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    if s[i] == p[j - 1] or p[j - 1] == ".":
                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = False

        return dp[len(s)][len(p)]

sol = Solution()

print(sol.isMatch("aa", "a"))
print(sol.isMatch("ab", ".*"))
print(sol.isMatch("aab", "c*a*b"))
print(sol.isMatch("mississippi", "mis*is*p*."))
