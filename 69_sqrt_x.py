class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        for i in range(1, x):
            div = x / i
            if div == i:
                return i
            elif div < i:
                return i - 1
        return 1

sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
print(sol.mySqrt(2))