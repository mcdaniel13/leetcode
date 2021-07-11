from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        interval = intervals[0]
        for i in range(1, len(intervals)):
            if interval[1] >= intervals[i][0]:
                interval[1] = max(interval[1], intervals[i][1])
            else:
                res.append(interval)
                interval = intervals[i]
        res.append(interval)
        return res

sol = Solution()
print(sol.merge([[1,4],[0,2],[3,5]]))
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))