from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.calculate(nums[:-1]), self.calculate(nums[1:]))
        
    def calculate(self, nums):
        dp = [0] * (len(nums) + 3)
        for i in range(len(nums)):
            dp[i + 3] = max(dp[i] + nums[i], dp[i + 1] + nums[i])
        return max(dp[-1], dp[-2])

sol = Solution()
print(sol.rob([1]))
print(sol.rob([2,3,2]))
print(sol.rob([1,2,3,1]))
print(sol.rob([1,2,3]))