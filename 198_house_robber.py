from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)

        for i in range(len(nums)):
            dp[i + 3] = max(dp[i], dp[i + 1]) + nums[i]

        return max(dp[-1], dp[-2])


sol = Solution()
print(sol.rob([1, 2, 3, 1]))
print(sol.rob([2, 7, 9, 3, 1]))
print(sol.rob([2, 1, 1, 2]))
