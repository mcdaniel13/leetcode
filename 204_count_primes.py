class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n + 1)
        if n <= 2:
            return 0

        for i in range(2, len(isPrime)):
            if isPrime[i] is True:
                for j in range(i + i, n, i):
                    isPrime[j] = False

        return isPrime[3:].count(True)


sol = Solution()
print(sol.countPrimes(10))
print(sol.countPrimes(0))
print(sol.countPrimes(1))
