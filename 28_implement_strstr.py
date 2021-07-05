class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

sol = Solution()
print(sol.strStr("hello", "ll"))
print(sol.strStr("aaaaa", "bba"))
print(sol.strStr("",""))