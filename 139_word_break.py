# Time Complexity: O(n^3)
# Space Complexity: O(n)

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            st = s[:i]
            for word in wordDict:
                if st.endswith(word) and dp[i - len(word)]:
                    dp[i] = True
                    break

        return dp[-1]

sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
print(sol.wordBreak("applepenapple", ["apple","pen"]))
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))