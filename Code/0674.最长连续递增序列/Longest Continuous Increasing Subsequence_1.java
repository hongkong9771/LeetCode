class Solution {
    public int findLengthOfLCIS(int[] nums) {
        /*
        dp[i]表示包含第i个元素的最长连续递增子序列的长度，每一个dp[i]都由其前面的一个数决定，即
        当nums[i]>nums[i-1]时，dp[i] = dp[i-1] + 1
        当nums[i]<=nums[i-1]，dp[i] = 1
        */

        int l = nums.length;
        // 动态数组初始化
        int[] dp = new int[l];
        Arrays.fill(dp, 1);
        // 动态传递
        int res = 1;
        for(int i = 1; i < l; i++){
            if (nums[i] > nums[i-1]){
                dp[i] = dp[i-1] + 1;
            }else{
                dp[i] = 1;
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}