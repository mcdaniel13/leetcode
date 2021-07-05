class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)

        if res < -2147483648 or res > 2147483647:
            return 2147483647

        return res


sol = Solution()
print(sol.divide(10, 3))
print(sol.divide(7, -3))
print(sol.divide(0, 1))
print(sol.divide(1, 1))