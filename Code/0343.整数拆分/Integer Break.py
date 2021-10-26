class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                '''
                j*(i-j)表示将i拆分成正整数j和i-j，并且不再拆分，此时的乘积为j*(i-j)
                j*dp[i-j]表示将i拆分成两个正整数j和i-j，并继续拆分i-j，此时的乘积为j*dp[i-j]
                其中i需要从2遍历至n，以统计每个正整数的整数拆分乘积最大值
                j需要从1遍历至i-1，以找到i的整数拆分乘积最大值，并每次更新最大值dp[i]
                '''
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])    
        return dp[n]