class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        li = []
        for i in range(numRows):
            li.append("")

        po = 0
        dr = True
        for ch in s:
            li[po] += ch
            if dr:
                if po == numRows - 1:
                    dr = False
                    po -= 1
                else:
                    po += 1
            else:
                if po == 0:
                    dr = True
                    po += 1
                else:
                    po -= 1

        return ''.join(li)

sol = Solution()

print(sol.convert("AB", 1))
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("A", 1))