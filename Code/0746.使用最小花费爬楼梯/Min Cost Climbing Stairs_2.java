class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // 此代码为对应的Java代码
        int l = cost.length;
        int[] dp = new int[2];

        // 初始化动态数组
        dp[0] = cost[0];
        dp[1] = cost[1];

        // 动态传递
        int temp;
        for(int i = 2; i < l; i++){
            // 采用压缩空间的做法
            temp = dp[1];
            dp[1] = Math.min(dp[0], dp[1]) + cost[i];
            dp[0] = temp;
            
            // dp[i] = Math.min(dp[i-1], dp[i-2]) + cost[i];
        }
        return Math.min(dp[0], dp[1]);
    }
}