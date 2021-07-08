from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one = False
        for i in range(len(nums)):
            if nums[i] == 1:
                one = True

        if one is False:
            return 1

        print("------")
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 1
        print(nums)
        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums) and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        print(nums)
        return len(nums) + 1

    def firstMissingPositiveAlternative(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[i] != i + 1:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1



sol = Solution()
# print(sol.firstMissingPositiveAlternative([1,2,0]))
print(sol.firstMissingPositiveAlternative([3,4,-1,1]))
print(sol.firstMissingPositiveAlternative([7,8,9,11,12]))
print(sol.firstMissingPositiveAlternative([0, 1,2]))