from typing import List


class MinStack:
    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return sorted(self.st)[0]


class Solution:
    def solve(self, comments: List[str], nums: List[int]):
        obj = MinStack()
        for i in range(1, len(comments)):
            if comments[i] == "push":
                obj.push(nums[i])
            elif comments[i] == "pop":
                obj.pop()
            elif comments[i] == "top":
                print(obj.top())
            elif comments[i] == "getMin":
                print(obj.getMin())
            else:
                continue


sol = Solution()
print(sol.solve(["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
                , [[], [-2], [0], [-3], [], [], [], []]))
