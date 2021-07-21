class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = [0] * (target + 1)

        # 初始化动态数组
        dp[0] = 1

        # 动态传递
        for i in range(1,target+1):
            for j in range(l):
                if nums[j] <= i:
                    dp[i] = dp[i] + dp[i - nums[j]]
                else:
                    dp[i] = dp[i]
        return dp[target]