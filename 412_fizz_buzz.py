class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            ans = ""
            if (i + 1) % 3 == 0:
                ans += "Fizz"

            if (i + 1) % 5 == 0:
                ans += "Buzz"

            if ans == "":
                ans += f"{i + 1}"

            res.append(ans)

        return res
