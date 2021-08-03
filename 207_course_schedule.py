from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, cur: int, graph: List[List[int]], isCycle: List[bool], visited: List[bool]) -> bool:
        if isCycle[cur] is False:
            return True

        if visited[cur] is True:
            return False

        visited[cur] = True
        for i in range(len(graph[cur])):
            if self.dfs(graph[cur][i], graph, isCycle, visited) is False:
                return False
            visited[graph[cur][i]] = False

        isCycle[cur] = False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        isCycle = [True] * numCourses
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])

        for i in range(numCourses):
            if isCycle[i]:
                if self.dfs(i, graph, isCycle, [False] * numCourses) is False:
                    return False

        return True

sol = Solution()
print(sol.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
print(sol.canFinish(2, [[1, 0], [0, 1]]))
