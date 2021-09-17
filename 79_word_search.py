from typing import List


class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def check(self, board: List[List[str]], word: str, idx: int, i: int, j: int, flag: List[List[bool]]) -> bool:
        if board[i][j] == word[idx]:
            flag[i][j] = True
            if idx == len(word) - 1:
                return True
        else:
            return False

        for k in range(4):
            if 0 <= i + self.dir[k][0] < len(board) and 0 <= j + self.dir[k][1] < len(board[i]) and \
                    flag[i + self.dir[k][0]][j + self.dir[k][1]] is False:
                if self.check(board, word, idx + 1, i + self.dir[k][0], j + self.dir[k][1], flag):
                    return True
        flag[i][j] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    flag = [[False] * len(board[i]) for i in range(len(board))]
                    if self.check(board, word, 0, i, j, flag):
                        return True

        return False


class Solution2:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.vLen = 0
        self.hLen = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.vLen = len(board)
        self.hLen = len(board[0])
        for i in range(self.vLen):
            for j in range(self.hLen):
                if board[i][j] == word[0] and self.dfs(board, i, j, word, 1):
                    return True
        return False

    def dfs(self, board: List[List[str]], i: int, j: int, word: str, wIdx: int) -> bool:
        if wIdx == len(word):
            return True

        temp = board[i][j]
        board[i][j] = "*"
        for k in range(4):
            ni = i + self.dir[k][0]
            nj = j + self.dir[k][1]
            if 0 <= ni < self.vLen and 0 <= nj < self.hLen \
                    and board[ni][nj] == word[wIdx] and self.dfs(board, ni, nj, word, wIdx + 1):
                return True

        board[i][j] = temp
        return False


sol = Solution2()
# print(sol.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
# print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
# print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
print(sol.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(sol.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
print(sol.exist([['a']], 'a'))
print(sol.exist([["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]], "aaaaaaaaaaaaa"))
