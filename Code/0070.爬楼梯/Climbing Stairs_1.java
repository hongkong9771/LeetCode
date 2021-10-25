class Solution {
    public int climbStairs(int n) {
        // 使用动态规划的方法做，与LC509题类似，斐波那契数列
        if(n <= 2){
            return n;
        }

        int[] dp = new int[2];
        // 初始化动态数组
        dp[0] = 1;
        dp[1] = 2;
        // 动态传递
        int temp;
        for(int i = 2; i < n; i++){
            temp = dp[1];
            dp[1] = dp[0] + dp[1];
            dp[0] = temp;

            // dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[1];
    }
}