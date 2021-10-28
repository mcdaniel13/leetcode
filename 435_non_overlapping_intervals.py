from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        arr = [intervals[0]]
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= arr[cnt - 1][1]: #overlapp
                arr.append(intervals[i])
                cnt += 1
        return len(intervals) - cnt

sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(sol.eraseOverlapIntervals([[1,2],[2,3]]))
print(sol.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))