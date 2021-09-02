from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] == target:
                start = mid + 1
            elif ord(letters[mid]) < ord(target):
                start = mid + 1
            else:
                end = mid - 1

        return letters[start % length]


sol = Solution()
print(sol.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"))
print(sol.nextGreatestLetter(["a", "c", "f", "j"], "a"))
print(sol.nextGreatestLetter(["a", "b", "c", "d", "f", "j"], "c"))
print(sol.nextGreatestLetter(["c", "f", "j"], "d"))
print(sol.nextGreatestLetter(["c", "d", "f", "j"], "g"))
print(sol.nextGreatestLetter(["c", "f", "j", "z"], "j"))
