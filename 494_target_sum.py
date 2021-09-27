from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cur = dict()
        cur[0] = 1

        start = 0
        while start < len(nums):
            next = dict()
            for k in cur:
                if nums[start] == 0:
                    for i in cur:
                        next[i] = cur[i] * 2
                else:
                    if k + nums[start] in next:
                        next[k + nums[start]] += cur[k]
                    else:
                        next[k + nums[start]] = cur[k]

                    if k - nums[start] in next:
                        next[k - nums[start]] += cur[k]
                    else:
                        next[k - nums[start]] = cur[k]
            cur = next
            start += 1

        if target in cur:
            return cur[target]
        else:
            return 0


sol = Solution()
print(sol.findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 1], 1))
print(sol.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(sol.findTargetSumWays([1], 1))
