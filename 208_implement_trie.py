from typing import List


class Trie:
    class TrieNode:
        def __init__(self):
            self.check = False
            self.alphabet = [None] * 26

    def __init__(self):
        self.head = self.TrieNode()

    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            idx = ord(ch) - 97
            if not cur.alphabet[idx]:
                cur.alphabet[idx] = self.TrieNode()
            cur = cur.alphabet[idx]

        cur.check = True

    def search(self, word: str) -> bool:
        cur = self.head
        for ch in word:
            idx = ord(ch) - 97
            if not cur.alphabet[idx]:
                return False
            cur = cur.alphabet[idx]

        return cur.check

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for ch in prefix:
            idx = ord(ch) - 97
            if not cur.alphabet[idx]:
                return False
            cur = cur.alphabet[idx]

        return True


class Solution:
    def solve(self, commends: List[str], params: List[str]) -> List[Optional[bool]]:
        obj = None
        res = []
        for i in range(len(commends)):
            if commends[i] == "insert":
                obj.insert(params[i])
                res.append(None)
            elif commends[i] == "search":
                res.append(obj.search(params[i]))
            elif commends[i] == "startsWith":
                res.append(obj.startsWith(params[i]))
            else:
                obj = Trie()
                res.append(None)

        return res


sol = Solution()
print(sol.solve(["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
                [[], "apple", "apple", "app", "app", "app", "app"]))
