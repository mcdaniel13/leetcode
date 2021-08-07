from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if 0 not in nums:
            return
        start = nums.index(0)

        end = nums.index(0)
        while end < len(nums):
            if nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
            end += 1


sol = Solution()
nums = [0, 1, 0, 3, 12]
print(sol.moveZeroes(nums))
print(nums)
nums = [0]
print(sol.moveZeroes(nums))
print(nums)
