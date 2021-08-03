class Solution:
    def reverseBits(self, n: int) -> int:
        s_bits = "{0:b}".format(n)[::-1]
        if len(s_bits) < 32:
            s_bits += "".join(['0' for i in range(32 - len(s_bits))])
        return int(s_bits, 2)


sol = Solution()
print(sol.reverseBits(int('00000010100101000001111010011100', 2)))
print(sol.reverseBits(int('11111111111111111111111111111101', 2)))
