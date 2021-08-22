from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[i] + 1:
                    dp[i] = max(dp[j] + 1, dp[i])

        maxi = 0

        for i in range(len(dp)):
            maxi = max(maxi, dp[i])

        return maxi


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
