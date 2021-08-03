class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        num_set.add(n)
        while n != 1:
            s_int = str(n)
            n = 0
            for ch in s_int:
                n += pow(int(ch), 2)

            if n in num_set:
                return False

            num_set.add(n)

        return True


sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))
