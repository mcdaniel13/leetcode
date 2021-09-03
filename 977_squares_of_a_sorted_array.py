class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        start = 0
        end = i = len(nums) - 1
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                res[i] = pow(nums[start], 2)
                start += 1
            else:
                res[i] = pow(nums[end], 2)
                end -= 1
            i -= 1

        return res

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        res = [pow(nums[i], 2) for i in range(len(nums))]
        return sorted(res)

    def sortedSquares3(self, nums: List[int]) -> List[int]:
        res1 = []
        res2 = []
        for i in range(len(nums)):
            if nums[i] < 0:
                res1.insert(0, pow(nums[i], 2))
            else:
                res2.append(pow(nums[i], 2))
        i1 = i2 = 0
        while i1 < len(res1) and i2 < len(res2):
            print(res1[i1], res2[i2])
            if res1[i1] > res2[i2]:
                res1.insert(i1, res2[i2])
                i2 += 1

            i1 += 1

        res1 += res2[i2:]
        return res1
