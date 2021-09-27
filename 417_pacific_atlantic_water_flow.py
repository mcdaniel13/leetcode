class Solution:
    def __init__(self):
        self.d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.n = 0
        self.m = 0

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])
        pacific = [[False] * self.n for _ in range(self.m)]
        atlantic = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if i == 0 or j == 0:
                    pacific[i][j] = True
                if i == self.m - 1 or j == self.n - 1:
                    atlantic[i][j] = True
                if pacific[i][j]:
                    visited = [[False] * self.n for _ in range(self.m)]
                    self.dfs(heights, i, j, pacific, visited)

                if atlantic[i][j]:
                    visited = [[False] * self.n for _ in range(self.m)]
                    self.dfs(heights, i, j, atlantic, visited)

        res = []
        for i in range(self.m):
            for j in range(self.n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, heights: List[List[int]], x: int, y: int, flag: List[List[bool]], visited: List[List[bool]]):
        for i in range(4):
            nx = x + self.d[i][0]
            ny = y + self.d[i][1]
            if 0 <= nx < self.m and 0 <= ny < self.n and heights[x][y] <= heights[nx][ny] and not visited[nx][
                ny] and not flag[nx][ny]:
                visited[nx][ny] = True
                flag[nx][ny] = flag[x][y]
                self.dfs(heights, nx, ny, flag, visited)