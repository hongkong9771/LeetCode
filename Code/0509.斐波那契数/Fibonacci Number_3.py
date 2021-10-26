class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]     # 相较于第二种解法而言，节约了空间成本，不需要储存整个斐波那契数列
        return dp[1]