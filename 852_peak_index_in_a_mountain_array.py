from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        start = 0
        end = length - 1
        res = 0
        while start <= end:
            mid = (start + end) // 2
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                start = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                end = mid - 1
            else:
                res = mid
                break

        return res


sol = Solution()
print(sol.peakIndexInMountainArray([0, 1, 0]))
print(sol.peakIndexInMountainArray([0, 2, 1, 0]))
print(sol.peakIndexInMountainArray([0, 10, 5, 2]))
print(sol.peakIndexInMountainArray([3, 4, 5, 1]))
print(sol.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
