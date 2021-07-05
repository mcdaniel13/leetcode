class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        res = 0
        for ch in s:
            idx = substr.find(ch)
            if idx != -1:
                res = max(res, len(substr))
                substr = substr[idx + 1:] + ch
            else:
                substr += ch

        return max(res, len(substr))

sol = Solution()

print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("dvdf"))
