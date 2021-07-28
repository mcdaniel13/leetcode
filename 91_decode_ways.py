class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 2)
        dp[0] = 0
        dp[1] = 1
        if s[0] == '0':
            return 0
        else:
            dp[2] = 1
        for i in range(1, len(s)):
            if 0 == int(s[i]):
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i + 2] = dp[i]
                else:
                    return 0
            else:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i + 2] = dp[i + 1] + dp[i]
                else:
                    dp[i + 2] = dp[i + 1]

        return dp[len(s) + 1]


sol = Solution()
print(sol.numDecodings("111110"))
print(sol.numDecodings("12201382"))
print(sol.numDecodings("230"))