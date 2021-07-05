from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        idx = (0, len(height) - 1, 0)
        while idx[0] < idx[1]:
            if height[idx[0]] < height[idx[1]]:
                idx = (idx[0] + 1, idx[1], max(idx[2], height[idx[0]] * (idx[1] - idx[0])))
            else:
                idx = (idx[0], idx[1] - 1, max(idx[2], height[idx[1]] * (idx[1] - idx[0])))
        return idx[2]


sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,1]))
print(sol.maxArea([4,3,2,1,4]))
print(sol.maxArea([1,2,1]))