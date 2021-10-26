class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        要满足题意，即从非空数组中选出一部分数组元素，使得这些数组元素的和为数组元素总和的一半
        一维dp数组表示，从数组下标为0-i的数组中选择部分元素，使得其和为j，若满足，则dp[j]=True
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
        dp = [False]*(S+1)
        dp[0] = True            # 不选取任何正整数，则被选取的正整数为0
        dp[nums[0]] = True

        # 动态传递
        for i in range(1, l):
            for j in range(S, 0, -1):
                if nums[i] == j:
                    dp[j] = True
                elif nums[i] < j:
                    dp[j] = dp[j] or dp[j-nums[i]]
                else:
                    dp[j] = dp[j]
        return dp[S]


