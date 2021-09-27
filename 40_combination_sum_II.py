from typing import List
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        key = sorted(counter)
        print(counter)
        res = []
        self.recursive(counter, key, target, [0], res)
        return res

    def recursive(self, counter: Counter, key: List[int], target: int, arr: List[int], res: List[List[int]]):
        if arr[0] == target:
            res.append(list(arr[1:]))
            return

        for i in range(len(key)):
            if counter[key[i]] == 0:
                continue
            if arr[0] + key[i] <= target:
                counter[key[i]] -= 1
                arr[0] += key[i]
                arr.append(key[i])
                if counter[key[i]] == 0:
                    self.recursive(counter, key[i + 1:], target, arr, res)
                else:
                    self.recursive(counter, key[i:], target, arr, res)
                arr.pop(-1)
                arr[0] -= key[i]
                counter[key[i]] += 1
            else:
                break


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
