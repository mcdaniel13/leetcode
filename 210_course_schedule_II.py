from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def dfs(self, cur: int, gr: List[List[int]], cycle: List[bool], visited: List[bool]) -> bool:
        if cycle[cur] is False:
            return True

        if visited[cur] is True:
            return False

        visited[cur] = True
        for i in range(len(gr[cur])):
            if self.dfs(gr[cur][i], gr, cycle, visited) is False:
                return False
            visited[gr[cur][i]] = False

        cycle[cur] = False
        self.res.append(cur)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        gr = [[] for i in range(numCourses)]
        self.res = []
        for pq in prerequisites:
            gr[pq[0]].append(pq[1])

        isCycle = [True] * numCourses
        for i in range(numCourses):
            if isCycle[i] and len(gr[i]) > 0:
                if self.dfs(i, gr, isCycle, [False] * numCourses) is False:
                    return []
            if len(self.res) == numCourses:
                return self.res

        if numCourses > 0 and len(self.res) < numCourses:
            for i in range(numCourses):
                if isCycle[i]:
                    self.res = [i] + self.res[:]

        return self.res


sol = Solution()
print(sol.findOrder(1, []))
print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
