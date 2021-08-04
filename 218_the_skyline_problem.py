from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        heights = set()
        for b in buildings:
            heights.add((b[0], -b[2]))
            heights.add((b[1], b[2]))
        res = []
        que = [0]
        prev_height = que[-1]
        heights = sorted(list(heights))

        for point, height in heights:
            if height < 0:
                que.append(-height)
                que.sort()
            else:
                que.pop(que.index(height))

            if que[-1] != prev_height:
                res.append([point, que[-1]])
                prev_height = que[-1]

        return res


sol = Solution()
print(sol.getSkyline([[2, 9, 10], [9, 12, 15]]))
print(sol.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]))
print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(sol.getSkyline([[0, 2, 3], [2, 5, 3]]))
