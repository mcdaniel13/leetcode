class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[1][1] = 1
        print(dp)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if i == 1 and j == 1:
                    continue

                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m][n]

sol = Solution()
print(sol.uniquePaths(3, 7))
print(sol.uniquePaths(3, 2))
print(sol.uniquePaths(7, 3))
print(sol.uniquePaths(3, 3))