class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n+1];
        int[] nums = new int[]{1,2};
        // 初始化动态数组
        dp[0] = 1;

        // 动态传递
        for(int i = 1; i <= n; i++){        //先遍历背包，再遍历物品
            for(int j = 0; j <= 1; j++){
                if(nums[j] <= i){
                    dp[i] += dp[i-nums[j]];
                }
            }
        }
        return dp[n];

    }
}