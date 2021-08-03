from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        return sorted(dic.items(), key=lambda item: item[1], reverse=True)[0][0]


sol = Solution()
print(sol.majorityElement([3, 2, 3]))
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
