class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        real_part = int(abs(numerator // denominator))

        res += str(real_part)

        frac_part = numerator % denominator
        if frac_part == 0:
            return res

        res += '.'
        dic = dict()
        while frac_part != 0:
            if frac_part in dic:
                res = res[:dic[frac_part]] + '(' + res[dic[frac_part]:] + ')'
                return res

            dic[frac_part] = len(res)

            frac_part *= 10
            res += str(frac_part // denominator)
            frac_part = frac_part % denominator

        return res


sol = Solution()
# print(sol.fractionToDecimal(1, 2))
# print(sol.fractionToDecimal(2, 1))
# print(sol.fractionToDecimal(2, 3))
# print(sol.fractionToDecimal(4, 333))
print(sol.fractionToDecimal(-50, 8))
