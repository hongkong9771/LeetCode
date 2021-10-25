class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i]表示包含第i个元素的子数组中的和最大值，只是以第i个元素结尾，并不一定从第1个元素开始
        对于dp[i]而言，若dp[i-1] > 0，则dp[i] = dp[i-1] + nums[i]，反之，dp[i] = nums[i]

        """

        l = len(nums)
        dp = [0] * l
        # 动态数组初始化
        dp[0] = nums[0]
        res = dp[0]
        # 动态传递过程
        for i in range(1, l):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
            res = max(res, dp[i])
        return res