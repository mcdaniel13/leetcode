from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.recursive(candidates, target, [0], res)
        return res

    def recursive(self, candidates: List[int], target: int, arr: List[int], res: List[List[int]]):
        if arr[0] == target:
            res.append(list(arr[1:]))
            return

        for i in range(len(candidates)):
            if arr[0] + candidates[i] <= target:
                if 0 < target - (arr[0] + candidates[i]) < candidates[i]:
                    continue
                arr[0] += candidates[i]
                arr.append(candidates[i])
                self.recursive(candidates[i:], target, arr, res)
                arr.pop(-1)
                arr[0] -= candidates[i]
            else:
                break


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.combinationSum([2, 3, 5], 8))
