# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        substr = ""
        ln = 0
        for idx, ch in enumerate(s):
            if s[idx - ln:idx + 1] == s[idx - ln:idx + 1][::-1]:
                substr = s[idx - ln:idx + 1]
                ln += 1
            elif idx - ln > 0 and s[idx - ln - 1:idx + 1] == s[idx - ln - 1:idx + 1][::-1]:
                substr = s[idx - ln - 1:idx + 1]
                ln += 2
        return substr


sol = Solution()

print(sol.longestPalindrome("cbbbbbd"))
print(sol.longestPalindrome("cbbbbd"))
print(sol.longestPalindrome("abababa"))
print(sol.longestPalindrome("ac"))
