from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = (nums[0], 0)

        for i in range(len(nums)):
            if res[0] < nums[i]:
                res = (nums[i], i)

        return res[1]


sol = Solution()
print(sol.findPeakElement([1, 2, 3, 1]))
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
