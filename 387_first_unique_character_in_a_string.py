import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = dict()
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1

        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i

        return -1


sol = Solution()
print(sol.firstUniqChar("a"))
print(sol.firstUniqChar("leetcode"))
print(sol.firstUniqChar("loveleetcode"))
print(sol.firstUniqChar("aabb"))