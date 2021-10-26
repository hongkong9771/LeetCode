class Solution {
    public int maxProfit(int[] prices, int fee) {
        /*
        dp[i][0]表示第i天持有股票的现金，dp[i][1]表示第i天不持有股票的现金。假设最开始的现金为0元
        则dp[i][0]可以分成两种情况：
        1）当天并未买入股票，则可能是由前一天购买的股票，所以dp[i][0] = dp[i-1][0]
        2）当天买入股票，所以dp[i][0] = dp[i-1] - price[i]   （此处是与LC121题的不通之处）
        dp[i][1]可以分成两种情况：
        1）当天并未卖出股票，则可能是前一天卖出的股票，所以dp[i][1] = dp[i-1][1]
        2）当天卖出股票，所以dp[i][1] = dp[i-1][0] + price[i] - fee     （此处完成一笔完整的交易，扣除手续费）         

        因为每一次的状态，只与前面的状态有关，因此，在此处可以采用压缩空间的做法
        */

        int l = prices.length;
        int[][] dp = new int[2][2];
        // 初始化动态数组
        dp[0][0] = -prices[0];
        dp[0][1] = 0;

        // 动态传递
        for(int i = 1;i < l;i++){
            dp[i % 2][0] = Math.max(dp[(i-1) % 2][0], dp[(i-1) % 2][1] - prices[i]);
            dp[i % 2][1] = Math.max(dp[(i-1) % 2][1], dp[(i-1) % 2][0] + prices[i] - fee);
        }
        return dp[(l-1) % 2][1];
    }
}