class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        res = []
        interval = firstList[0]
        for i in range(len(firstList) + len(secondList)):
            


sol = Solution()
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(sol.intervalIntersection(firstList, secondList))

firstList = [[1,3],[5,9]]
secondList = []
print(sol.intervalIntersection(firstList, secondList))

firstList = []
secondList = [[4,8],[10,12]]
print(sol.intervalIntersection(firstList, secondList))

firstList = [[1,7]]
secondList = [[3,10]]
print(sol.intervalIntersection(firstList, secondList))
