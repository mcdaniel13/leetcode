from typing import List


class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            for i in range(4):
                nx = dir[i][0] + x
                ny = dir[i][1] + y
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    grid[nx][ny] = 'X'
                    dfs(nx, ny)

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = 'X'
                    dfs(i, j)
                    res += 1

        return res

    def numIslands_bfs(self, grid: List[List[str]]) -> int:
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

    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            for k in range(len(dr)):
                ni = i + dr[k][0]
                nj = j + dr[k][1]
                if 0 <= ni < vn and 0 <= nj < hn and grid[ni][nj] == '1':
                    grid[ni][nj] = 'X'
                    dfs(ni, nj)

        dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        vn = len(grid)
        hn = len(grid[0])
        cnt = 0
        for i in range(vn):
            for j in range(hn):
                if grid[i][j] == '1':
                    grid[i][j] = 'X'
                    dfs(i, j)
                    cnt += 1
        return cnt


sol = Solution()
print(sol.numIslands_dfs([["1", "0"]]))
print(sol.numIslands_dfs([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(sol.numIslands_dfs([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
