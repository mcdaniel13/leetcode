from typing import List


class Solution:
    def __init__(self):
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def solve(self, board: List[List[str]]) -> None:
        flag = [[False] * len(board[0]) for i in range(len(board))]
        for i in range(len(board[0])):
            if board[0][i] == "O" and not flag[0][i]:
                flag[0][i] = True
                self.scan(board, flag, [0, i])
            if board[len(board) - 1][i] == "O" and not flag[len(board) - 1][i]:
                flag[len(board) - 1][i] = True
                self.scan(board, flag, [len(board) - 1, i])

        for i in range(len(board)):
            if board[i][0] == "O" and not flag[i][0]:
                flag[i][0] = True
                self.scan(board, flag, [i, 0])
            if board[i][len(board[0]) - 1] == "O" and not flag[i][len(board[0]) - 1]:
                flag[i][len(board[0]) - 1] = True
                self.scan(board, flag, [i, len(board[0]) - 1])

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and not flag[i][j]:
                    board[i][j] = "X"

    def scan(self, board: List[List[str]], flag: List[List[bool]], cord: List[int]) -> None:
        for i in range(4):
            v = self.dir[i][0] + cord[0]
            h = self.dir[i][1] + cord[1]
            if 0 <= v < len(board) and 0 <= h < len(board[0]) and board[v][h] == "O" and not flag[v][h]:
                flag[v][h] = True
                self.scan(board, flag, [v, h])


sol = Solution()
board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
sol.solve(board)
print(board)

board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
sol.solve(board)
print(board)
