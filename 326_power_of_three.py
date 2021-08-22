class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            q1 = n / 3
            q2 = n // 3
            if q1 == q2:
                n = q2
            else:
                return False

        return n > 0

sol = Solution()
print(sol.isPowerOfThree(27))
print(sol.isPowerOfThree(0))
print(sol.isPowerOfThree(9))
print(sol.isPowerOfThree(45))