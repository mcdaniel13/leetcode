from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums[idx1 + 1:], idx1 + 1):
                if val1 + val2 == target:
                    return [idx1, idx2]


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
