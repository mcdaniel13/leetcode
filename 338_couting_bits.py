from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            cnt[i] = cnt[i//2] + i % 2

        return cnt

sol = Solution()
print(sol.countBits(2))
print(sol.countBits(5))
