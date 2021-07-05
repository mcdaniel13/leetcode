class Solution:
    def reverse(self, x: int) -> int:
        if int(x / 10) == 0:
            return x
        negative = False
        if x < 0:
            x *= -1
            negative = True

        s = str(x)
        s = s[::-1]
        i = int(s)
        if negative is True:
            i *= -1

        if i >= int(2**31 - 1) or i <= int(-2**31):
            i = 0
        return i


sol = Solution()

print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
print(sol.reverse(1534236469))
