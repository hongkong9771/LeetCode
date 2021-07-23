class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        因为相邻两个房子不能被同时偷窃，所以，如果下一间房被偷窃了，则上一间房一定不能被偷窃，
        如果下一间房被偷窃了，则上一间房可能被偷窃
        """
        
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]

        dp = [0] * (l)
        # 初始化动态数组
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 动态传递
        for i in range(2,l):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[l-1]