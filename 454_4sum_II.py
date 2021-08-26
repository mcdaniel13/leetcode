from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dic = dict()
        for num1 in nums1:
            for num2 in nums2:
                sum = num1 + num2
                if sum in dic:
                    dic[sum] += 1
                else:
                    dic[sum] = 1

        res = 0
        for num3 in nums3:
            for num4 in nums4:
                sum = -(num3 + num4)
                if sum in dic:
                    res += dic[sum]

        return res


sol = Solution()
print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
print(sol.fourSumCount([0], [0], [0], [0]))
