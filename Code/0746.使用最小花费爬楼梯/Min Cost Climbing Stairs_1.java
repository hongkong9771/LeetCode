class Solution {
    public int minCostClimbingStairs(int[] cost) {
        // 此代码为对应的Java代码
        int l = cost.length;
        int[] dp = new int[l];

        // 初始化动态数组
        dp[0] = cost[0];
        dp[1] = cost[1];

        // 动态传递
        for(int i = 2; i < l; i++){
            dp[i] = Math.min(dp[i-1], dp[i-2]) + cost[i];
        }
        return Math.min(dp[l-2], dp[l-1]);
    }
}