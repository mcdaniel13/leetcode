from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempMax = nums[0]
        ansMax = nums[0]
        for i in range(1, len(nums)):
            tempMax = max(nums[i], tempMax + nums[i])
            ansMax = max(tempMax, ansMax)

        return ansMax

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5,4,-1,7,8]))