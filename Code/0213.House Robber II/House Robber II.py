class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        此题和lc198题是一样的，只不过在首尾两端成环了，因此，可以分成两种情况来考虑：
        1）包含首元素---尾元素之前（即不包含尾元素）
        2）首元素之后---尾元素---（即不包含首元素）
        比较两种情况的金额，取最大值
        因为相邻两个房子不能被同时偷窃，所以，如果下一间房被偷窃了，则上一间房一定不能被偷窃，
        如果下一间房被偷窃了，则上一间房可能被偷窃
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        amount1 = self.rob_1(nums[:l-1])
        amount2 = self.rob_1(nums[1:])
        return max(amount1, amount2)


    def rob_1(self,nums_1):
        l = len(nums_1)

        if l == 0:
            return 0
        elif l == 1:
            return nums_1[0]
        
        dp = [0] * l
        dp[0] = nums_1[0]
        dp[1] = max(nums_1[0], nums_1[1])

        for i in range(2,l):
            dp[i] = max(dp[i-1], dp[i-2]+nums_1[i])
        return dp[-1]
