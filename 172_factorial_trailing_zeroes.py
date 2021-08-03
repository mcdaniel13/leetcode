class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n //= 5
            res += n

        return res



sol = Solution()
print(sol.trailingZeroes(3))
print(sol.trailingZeroes(5))
print(sol.trailingZeroes(0))