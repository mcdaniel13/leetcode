class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + 1

        base = 2
        while pow(base, 2) <= n:
            idx = pow(base, 2)
            dp[idx] = 1
            for i in range(idx + 1, len(dp)):
                dp[i] = min(dp[i], dp[i - idx] + 1)
            base += 1

        return dp[n]


sol = Solution()
print(sol.numSquares(12))
print(sol.numSquares(13))
