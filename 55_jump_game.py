from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx = 0
        for i in range(len(nums)):
            if maxIdx >= i:
                maxIdx = max(maxIdx, i + nums[i])

        return maxIdx >= len(nums) - 1

sol = Solution()
# print(sol.canJump([1]))
print(sol.canJump([0,2,3]))
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))