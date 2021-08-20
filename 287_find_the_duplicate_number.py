from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        for i in range(len(nums)):
            if nums[i] in num_set:
                return nums[i]
            else:
                num_set.add(nums[i])

        return -1


sol = Solution()
print(sol.findDuplicate([1, 3, 4, 2, 2]))
print(sol.findDuplicate([3, 1, 3, 4, 2]))
print(sol.findDuplicate([1, 1]))
print(sol.findDuplicate([1, 1, 2]))
