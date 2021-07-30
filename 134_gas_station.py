from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        remains = []
        idxs = []
        for i in range(len(gas)):
            remain = gas[i] - cost[i]
            if remain >= 0:
                idxs.append(i)
            remains.append(remain)

        for i in range(len(idxs)):
            if self.check(remains[idxs[i]:] + remains[:idxs[i]]):
                return idxs[i]

        return -1

    def check(self, li: List[int]):
        sum = 0
        for val in li:
            sum += val
            if sum < 0:
                return False
        return True


sol = Solution()
print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
