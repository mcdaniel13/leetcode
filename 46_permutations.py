from typing import List


class Solution:
    def getRecursively(self, nums: List[int], arr: List[int], res: List[List[int]]) -> None:
        if len(nums) == 0:
            res.append(arr)
            return

        for i in range(len(nums)):
            self.getRecursively(nums[:i] + nums[i + 1:], arr + nums[i:i+1], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.getRecursively(nums, [], res)
        return res


sol = Solution()
print(sol.permute([1,1, 2]))
print(sol.permute([0,1]))
print(sol.permute([1]))