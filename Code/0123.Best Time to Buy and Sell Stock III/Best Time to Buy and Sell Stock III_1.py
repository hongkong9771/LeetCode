class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        因为本题可以至多两次买卖股票，所以一共有五种状态，
        dp[i][j]表示第i天进行j操作后的现金，其中j操作表示：没有操作、第一次买入、第一次卖出、第二次买入、第二次卖出
        分别用0, 1, 2, 3, 4来表示
        1.dp[i][0]表示第i天没有任何操作，所以dp[i][0] = dp[i-1][0]
        2.dp[i][1]表示第i天为第一次买入状态，则：
            1）可能前一天就已经买入了，所以dp[i][1] = dp[i-1][1]
            2）第i天才买入的，所以dp[i][1] = dp[i-1][0] - prices[i]
        3.dp[i][2]表示第i天为第一次卖出状态，则：
            1）可能前一天就已经卖出了，所以dp[i][2] = dp[i-1][2]
            2）第i天才卖出的，所以dp[i][2] = dp[i-1][1] + prices[i]
        4.dp[i][3]表示第i天为第二次买入状态，则：
            1）可能前一天就已经买入了，所以dp[i][3] = dp[i-1][3]
            2）第i天才买入的，所以dp[i][3] = dp[i-1][2] - prices[i]
        3.dp[i][4]表示第i天为第一次卖出状态，则：
            1）可能前一天就已经卖出了，所以dp[i][4] = dp[i-1][4]
            2）第i天才卖出的，所以dp[i][4] = dp[i-1][3] + prices[i]

        """

        l = len(prices)
        dp = [[0] * 5 for _ in range(l)]
        # 初始化动态数组
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        # 动态传递
        for i in range(1, l):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i][0]-prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
        return max(dp[l-1][2], dp[l-1][4])

