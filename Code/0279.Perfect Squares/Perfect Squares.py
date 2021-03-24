class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = i       # 最差的情况就是全部由1组成，数量为i
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i-j*j] + 1, dp[i])
                j += 1
        return dp[-1]