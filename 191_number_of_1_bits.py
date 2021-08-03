class Solution:
    def hammingWeight(self, n: int) -> int:
        s_bits = "{0:b}".format(n)
        return s_bits.count('1')


sol = Solution()
print(sol.hammingWeight(int('00000000000000000000000000001011', 2)))
print(sol.hammingWeight(int('00000000000000000000000010000000', 2)))
print(sol.hammingWeight(int('11111111111111111111111111111101', 2)))
