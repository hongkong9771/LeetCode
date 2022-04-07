class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        此题是LC53.最大子数组和的一个进阶题，因为需要考虑到整数的正负。因此，在记录乘积最大时，需要同时记录最大值和最小值，才能保证最终的值为最大值，二维数组中的dp[0]用于记录最大值，dp[1]用于记录最小值
        则有：
        dp[0][i] = max(dp[0][i]*nums[i], nums[i], dp[1][i]*nums[i])
        dp[1][i] = min(dp[1][i]*nums[i], nums[i], dp[0][i]*nums[i])
        """
        n = len(nums)

        # 动态数组初始化
        dp = [[0] * n for _ in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        res = nums[0]

        # 动态传递过程
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1]*nums[i], nums[i], dp[1][i-1]*nums[i])
            dp[1][i] = min(dp[1][i-1]*nums[i], nums[i], dp[0][i-1]*nums[i])
            res = max(res, dp[0][i])
        return res