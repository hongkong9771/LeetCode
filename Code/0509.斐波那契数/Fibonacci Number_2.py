class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        for i in range(n-1):
            dp.append(dp[-2]+dp[-1])
        return dp[n]