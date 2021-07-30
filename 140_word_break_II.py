from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        self.dfs(s, wordDict, "", res)
        return res

    def dfs(self, s: str, wordDict: List[str], sub: str, res: List[str]):
        if s == "":
            res.append(sub[1:])
            return

        for i in range(1, len(s) + 1):
            st = s[:i]
            if st in wordDict:
                self.dfs(s[i:], wordDict, sub + " " + st, res)


sol = Solution()
print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))