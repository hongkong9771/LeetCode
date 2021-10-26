class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        dp[i]表示包含第i个元素的最长连续递增子序列的长度，每一个dp[i]都由其前面的一个数决定，即
        当nums[i]>nums[i-1]时，dp[i] = dp[i-1] + 1
        当nums[i]<=nums[i-1]，dp[i] = 1
        """
        l = len(nums)
        # 动态数组初始化
        dp = [1] * l
        # 动态传递
        res = 1
        for i in range(1, l):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
            res = max(res, dp[i])
        return res