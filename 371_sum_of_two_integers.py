class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b

        if b == 0:
            return a

        mask = 0xffffffff
        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = carry << 1

        if a >> 31 & 1:
            a = ~(a ^ mask)

        return a


sol = Solution()
print(sol.getSum(-12, -8))
print(sol.getSum(1, -1))
print(sol.getSum(1, 2))
print(sol.getSum(2, 3))
