from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, [], res, 0)
        return list(res)

    def dfs(self, nums: List[int], cur: List[int], res: List[List[int]], idx: int):
        if idx == len(nums):
            arr = cur[:]
            res.append(arr)
            return

        cur.append(nums[idx])
        self.dfs(nums, cur, res, idx + 1)
        cur.pop()
        while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
            idx += 1

        self.dfs(nums, cur, res, idx + 1)


sol = Solution()
print(sol.subsetsWithDup([4, 4, 4, 1, 4]))
print(sol.subsetsWithDup([1, 2, 2]))
print(sol.subsetsWithDup([0]))
