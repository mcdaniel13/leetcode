from typing import List
from bisect import insort


class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        insort(self.arr, num)

    def findMedian(self) -> float:
        idx = len(self.arr) // 2
        if len(self.arr) % 2 == 0:
            return (self.arr[idx - 1] + self.arr[idx]) / 2
        else:
            return self.arr[idx]


class Solution:
    def __init__(self):
        self.medianFinder = None

    def solve(self, commends: List[str], nums: List[List[int]]):
        res = []
        for i in range(len(commends)):
            if commends[i] == "MedianFinder":
                self.medianFinder = MedianFinder()
                res.append(None)
            elif commends[i] == "addNum":
                self.medianFinder.addNum(nums[i][0])
                res.append(None)
            else:
                res.append(self.medianFinder.findMedian())

        return res


sol = Solution()
print(sol.solve(["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
                [[], [1], [2], [], [3], []]))
print(sol.solve(
    ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian"],
    [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]))

print(sol.solve(
    ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
     "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
     "findMedian", "addNum", "findMedian"]
    , [[], [1], [], [2], [], [3], [], [4], [], [5], [], [6], [], [7], [], [8], [], [9], [], [10], []]))
