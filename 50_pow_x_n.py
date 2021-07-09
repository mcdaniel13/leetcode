class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)


sol = Solution()
print(sol.myPow(2.00000, 10))
print(sol.myPow(2.10000, 3))
print(sol.myPow(2.00000, -2))