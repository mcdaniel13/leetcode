from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[i])):
                cnt = 0
                if i + 1 < len(board):
                    cnt += board[i + 1][j] % 2
                    if j + 1 < len(board[i]):
                        cnt += board[i + 1][j + 1] % 2
                    if 0 <= j - 1:
                        cnt += board[i + 1][j - 1] % 2
                if 0 <= i - 1:
                    cnt += board[i - 1][j] % 2
                    if 0 <= j - 1:
                        cnt += board[i - 1][j - 1] % 2
                    if j + 1 < len(board[i]):
                        cnt += board[i - 1][j + 1] % 2
                if j + 1 < len(board[i]):
                    cnt += board[i][j + 1] % 2
                if 0 <= j - 1:
                    cnt += board[i][j - 1] % 2

                if board[i][j] == 1 and not 2 <= cnt <= 3:
                    board[i][j] = 3
                elif board[i][j] == 0 and cnt == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


sol = Solution()

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
sol.gameOfLife(board)
print(board)

board = [[1, 1], [1, 0]]
sol.gameOfLife(board)
print(board)
