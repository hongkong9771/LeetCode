class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[i]表示数组长度为i的数组中最长严格递增子序列的长度，则每一个dp[i]都可以由dp[j]（i>j）计算得到。
        其中j需要从0遍历至i-1，以从中找到最大的递增子序列长度

        """
        l = len(nums)
        # 动态数组初始化
        dp = [1] * l
        # 动态传递
        res = 1
        for i in range(1, l):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)     # 更新dp[i]为最大值
            res = max(res, dp[i])
        return res