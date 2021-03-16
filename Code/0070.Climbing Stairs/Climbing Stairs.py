class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n <= 2:
            return dp[n-1]
        for i in range(3, n+1):
            dp[0], dp[1] = dp[1], dp[0]+dp[1]       # 相较于下面代码而言，节约了空间成本，不需要储存整个爬楼梯的情况
            # dp[i] = dp[i-1] + dp[i-2]
        return dp[1]