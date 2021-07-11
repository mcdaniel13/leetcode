from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        bigger = True
        for i in range(len(digits) - 1, -1, -1):
            if bigger:
                digits[i] += 1

            if digits[i] >= 10:
                bigger = True
                digits[i] -= 10
            else:
                bigger = False

        if bigger:
            digits = [1] + digits
        return digits

sol = Solution()
print(sol.plusOne([1,2,3]))
print(sol.plusOne([4,3,2,1]))
print(sol.plusOne([0]))
print(sol.plusOne([9]))