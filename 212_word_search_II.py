from typing import List, Tuple
from collections import defaultdict


class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.res = []

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = self.makeTrieTree(words)

        self.res = []

        visited = [[False] * len(board[0]) for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                visited[i][j] = True
                self.dfs(head, board, visited, i, j)
                visited[i][j] = False

        return self.res

    def makeTrieTree(self, words: List[str]) -> dict:
        head = dict()
        for word in words:
            cur = head
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['!'] = word

        return head

    def dfs(self, cur: dict, board: List[List[str]], visited: List[List[bool]], i: int, j: int) -> None:
        if board[i][j] not in cur:
            return

        cur = cur[board[i][j]]

        if '!' in cur:
            self.res.append(cur['!'])
            del cur['!']

        for k in range(len(self.dir)):
            ni = i + self.dir[k][0]
            nj = j + self.dir[k][1]
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not visited[ni][nj]:
                visited[ni][nj] = True
                self.dfs(cur, board, visited, ni, nj)
                visited[ni][nj] = False


sol = Solution()
print(sol.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                    ["oath", "pea", "eat", "rain"]))
print(sol.findWords([["a", "b"], ["c", "d"]], ["abcb"]))
