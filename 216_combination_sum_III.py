from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k >= n != 1 and n > 45:
            return []
        res = []
        self.recursive(k, n, 1, [0], res)
        return res

    def recursive(self, k: int, n: int, start: int, arr: List[int], res: List[List[int]]):
        if k == 0:
            if n == arr[0]:
                res.append(list(arr[1:]))
            return

        for i in range(start, 10):
            if arr[0] + i <= n:
                if 0 < n - (arr[0] + i) <= i:
                    continue
                if arr[0] + i == n and k - 1 != 0:
                    break
                arr[0] += i
                arr.append(i)
                self.recursive(k - 1, n, i + 1, arr, res)
                arr.pop(-1)
                arr[0] -= i
            else:
                break


sol = Solution()
print(sol.combinationSum3(3, 7))
print(sol.combinationSum3(3, 9))
print(sol.combinationSum3(4, 1))
print(sol.combinationSum3(3, 2))
print(sol.combinationSum3(9, 45))
