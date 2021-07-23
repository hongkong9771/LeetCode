class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp[i][0]表示第i天持有股票的现金，dp[i][1]表示第i天不持有股票的现金。假设最开始的现金为0元
        则dp[i][0]可以分成两种情况：
        1）当天并未买股票，则可能是由前一天购买的股票，所以dp[i][0] = dp[i-1][0]
        2）当天购买了股票，所以dp[i][0] = -prices[i]
        dp[i][1]可以分成两种情况：
        1）当天并未卖出股票，则可能是由前一天卖出的股票，所以dp[i][1] = dp[i-1][1]
        2）当天卖出了股票，所以dp[i][0] = prices[i] + dp[i-1][0]


        因为，每次买卖股票都只与前一天的状态有关，所以下面采用压缩空间的做法  
        """
        l = len(prices)
        dp = [[0] * 2] * 2
        # 初始化动态数组
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        # 动态传递
        for i in range(1,l):
            dp[i%2][0] = max(dp[(i-1)%2][0], -prices[i])        # 持有股票
            dp[i%2][1] = max(dp[(i-1)%2][1], prices[i]+dp[(i-1)%2][0]) # 不持有股票

            # dp[i][0] = max(dp[i-1][0], -prices[i])      # 持有股票
            # dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])  # 不持有股票
        return dp[(l-1)%2][1]