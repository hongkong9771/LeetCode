class Solution {
    public int fib(int n) {
        if(n <= 1){
            return n;
        }
        int[] dp = new int[2];
        // 动态数组初始化
        dp[0] = 0;
        dp[1] = 1;
        // 动态传递
        int temp;
        for(int i = 2;i <= n; i++){
            temp = dp[1];
            dp[1] = dp[0] + dp[1];
            dp[0] = temp;
            // dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[1];
    }
}