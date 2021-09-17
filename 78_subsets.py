from typing import List


class Solution:
    def findSubset(self, nums: List[int], cur: List[int], res: List[List[int]], start: int) -> None:
        if start == len(nums):
            return

        for i in range(start, len(nums)):
            arr = cur[:]
            arr.append(nums[i])
            res.append(arr)
            self.findSubset(nums, arr, res, i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        self.findSubset(nums, [], res, 0)
        return res


sol = Solution()
print(sol.subsets([1,2,3]))
print(sol.subsets([0]))