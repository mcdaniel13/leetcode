from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack = [-1]
        res = 0
        for i in range(len(heights)):
            while len(stack) != 0 and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                h = heights[idx]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res


sol = Solution()
print(sol.largestRectangleArea([2, 1, 2]))
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(sol.largestRectangleArea([2, 4]))
