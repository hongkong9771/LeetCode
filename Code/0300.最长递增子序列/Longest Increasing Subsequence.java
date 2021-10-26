class Solution {
    public int lengthOfLIS(int[] nums) {
        /*
        dp[i]表示包含第i个元素的最长严格递增子序列的长度，则每一个dp[i]都可以由dp[j]（i>j）计算得到。
        其中j需要从0遍历至i-1，以从中找到最大的递增子序列长度
        */
        int l = nums.length;
        // 初始化动态数组
        int[] dp = new int[l];
        // Arrays.fill(dp, 1);     // 给数组的元素赋固定的值
        for(int i = 0; i < l; i++){
            dp[i] = 1;
        }
        
        // 动态传递
        int res = 1;
        for(int i = 1; i < l; i++){
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j])
                {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                } 
            }
            res = Math.max(res, dp[i]);        
        }
        return res;
    }
}