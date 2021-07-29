from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur = prices[0]
        for i in range(1, len(prices)):
            if cur >= prices[i]:
                cur = prices[i]
            else:
                res += prices[i] - cur
                cur = prices[i]

        return res

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([1, 2, 3, 4, 5]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
