import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                if dp[i - c] != sys.maxsize:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[-1] if dp[-1] != sys.maxsize else -1


sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([1], 0))
print(sol.coinChange([1], 1))
print(sol.coinChange([1], 2))
