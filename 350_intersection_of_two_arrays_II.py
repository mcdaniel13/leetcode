from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = dict()
        for num in nums1:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        res = []
        for num in nums2:
            if num in dic:
                if dic[num] != 0:
                    res.append(num)
                    dic[num] -= 1

        return res


sol = Solution()
print(sol.intersect([1, 2, 2, 1], [2, 2]))
print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
