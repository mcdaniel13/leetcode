import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pr = [0, 0]
        res = 0
        for i in range(1, len(prices)):
            if prices[pr[0]] <= prices[i] or pr[0] < pr[1] and prices[pr[1]] < prices[i]:
                pr[0] = i

            if prices[pr[1]] >= prices[i]:
                pr[1] = i

            if pr[0] > pr[1]:
                res = max(res, prices[pr[0]] - prices[pr[1]])

        return res

    def maxProfit2(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
