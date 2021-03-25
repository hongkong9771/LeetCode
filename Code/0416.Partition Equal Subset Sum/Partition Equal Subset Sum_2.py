class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        要满足题意，即从非空数组中选出一部分数组元素，使得这些数组元素的和为数组元素总和的一半
        二维dp数组表示，从数组下标为0-i的数组中选择部分元素，使得其和为j，若满足，则dp[i][j]=True
        '''
        S = int(sum(nums)/2)
        l = len(nums)
        # 当数组元素的和为奇数时，不满足条件
        if sum(nums)%2 == 1:
            return False
        # 当数组中的最大元素大于数组和的一半时，不满足条件
        if max(nums) > S:
            return False
        # 当数组元素个数小于2时，无法被分为两个子集，不满足条件
        if l < 2:
            return False
        # 初始化动态数组
        dp = [[False]*(S+1) for _ in range(l)]
        for i in range(l):
            dp[i][0] = True
        if nums[0] <= S:
            dp[0][nums[0]] = True

        # 动态传递
        for i in range(l):
            for j in range(1, S+1):
                if nums[i] == j:
                    dp[i][j] = True
                elif nums[i] < j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[l-1][S]
