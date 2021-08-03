from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = nums[:]
        rot = k % len(nums)

        if rot == 0:
            return

        for i in range(len(nums)):
            nums[i] = temp[(len(nums) - rot + i) % len(nums)]


sol = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, 4)
print(nums)

nums = [-1, -100, 3, 99]
sol.rotate(nums, 2)
print(nums)
