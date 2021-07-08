from typing import List


class Solution:
    def getIndex(self, i: int, j: int) -> int:
        if j <= 2:
            if i <= 2:
                return 0
            elif i <= 5:
                return 1
            else:
                return 2
        elif j <= 5:
            if i <= 2:
                return 3
            elif i <= 5:
                return 4
            else:
                return 5
        else:
            if i <= 2:
                return 6
            elif i <= 5:
                return 7
            else:
                return 8

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = [[False] * 9 for i in range(9)]
        vertical = [[False] * 9 for i in range(9)]
        three = [[False] * 9 for i in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                # print("======== i =", i, " j=", j, "========")
                if board[i][j] == ".":
                    continue
                else:
                    val = int(board[i][j]) - 1
                    if horizontal[j][val] is False:
                        # print("horizontal become True at val =", val)
                        horizontal[j][val] = True
                    else:
                        # print("horizontal already True val =", val, "- False")
                        return False
                    # print(horizontal)

                    if vertical[i][val] is False:
                        # print("vertical become True at val =", val)
                        vertical[i][val] = True
                    else:
                        # print("vertical already True val =", val, "- False")
                        return False
                    # print(vertical)

                    idx = self.getIndex(i, j)
                    if three[idx][val] is False:
                        # print("three become True at val =", val)
                        three[idx][val] = True
                    else:
                        # print("three already True val =", val, "- False")
                        return False
                    # print(three)

        return True

sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
