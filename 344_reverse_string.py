from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s) - 1
        for i in range(int(size / 2) + 1):
            s[i], s[size - i] = s[size - i], s[i]
