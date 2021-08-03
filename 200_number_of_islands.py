from typing import List


class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    grid[i][j] = 'X'
                    res += 1
                    que = [(i, j)]
                    while que:
                        cord = que.pop(0)
                        for k in range(4):
                            ncord = (cord[0] + self.dir[k][0], cord[1] + self.dir[k][1])
                            if 0 <= ncord[0] < len(grid) and 0 <= ncord[1] < len(grid[0]) \
                                    and grid[ncord[0]][ncord[1]] == '1':
                                grid[ncord[0]][ncord[1]] = 'X'
                                que.append(ncord)
        return res

sol = Solution()
print(sol.numIslands([["1", "0"]]))
print(sol.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(sol.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))