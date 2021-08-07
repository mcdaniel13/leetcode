from typing import List
from bisect import insort


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = []
        res = []
        for i in range(len(nums)):
            if que and i - que[0] == k:
                que.pop(0)
            while que:
                if nums[que[-1]] < nums[i]:
                    que.pop(-1)
                else:
                    break
            que.append(i)
            if i >= k - 1:
                res.append(nums[que[0]])
        return res


sol = Solution()
print(sol.maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sol.maxSlidingWindow([1], 1))
print(sol.maxSlidingWindow([1, -1], 1))
print(sol.maxSlidingWindow([9, 11], 2))
print(sol.maxSlidingWindow([4, -2], 2))
