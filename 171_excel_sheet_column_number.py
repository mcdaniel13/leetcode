class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        j = 0
        for i in range(len(columnTitle) - 1, -1, -1):
            res += pow(26, j) * (ord(columnTitle[i]) - 64)
            j += 1

        return res


sol = Solution()
print(sol.titleToNumber("A"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))
print(sol.titleToNumber("FXSHRXW"))
