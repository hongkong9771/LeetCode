class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        二刷：采用压缩数组的方式
        dp[i]表示包含当前整数的最大子数组的和，则dp[i]的值分为以下两种情况：
        1) 当dp[i-1]>0时，dp[i]=dp[i-1]+nums[i]
        2) 当dp[i-1]<=0时，dp[i]=nums[i]
        
        """
        n = len(nums)
        Max_sum, dp = nums[0], nums[0]
        for i in range(1, n):
            if dp > 0:
                dp = dp + nums[i]
            else:
                dp = nums[i]
            Max_sum = max(Max_sum, dp)
        return Max_sum