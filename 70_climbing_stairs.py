class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i - 1] + steps[i - 2])

        return steps[n - 1]

sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))