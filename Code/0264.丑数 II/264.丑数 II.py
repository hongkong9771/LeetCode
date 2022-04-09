class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        新的丑数由之前的丑数乘以2、3、5之中的一个得到（保证质因子永远只有2、3、5），
        我们可以维护三个坐标，记录每个质因子现在该乘的是第几个丑数。
        """
        dp = [1] * n

        index2, index3, index5 = 0, 0, 0

        for i in range(1, n):
            dp[i] = min(dp[index2]*2, dp[index3]*3, dp[index5]*5)
            if dp[i] == dp[index2]*2:
                index2 += 1
            if dp[i] == dp[index3]*3:
                index3 += 1
            if dp[i] == dp[index5]*5:
                index5 += 1
        return dp[n-1]
