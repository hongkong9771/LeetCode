class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        此题与LC152.乘积最大子数组类似，需要同时维护两个数组用于分别统计正负情况，
        dp[0][i]表示包含第i个元素的乘积为正数的最长子数组长度，dp[1][i]表示包含第i个元素的乘积为负数的最长子数组的长度
        首先，对于动态数组的初始化而言，当nums[0]>0时，dp[0][0]=1, dp[1][0]=0，反之则相反。
        共包含以下几种情况：
        1) 当nums[i]>0时
            dp[0][i] = dp[0][i-1] + 1
            当dp[1][i-1]>0时，dp[1][i] = dp[1][i-1] + 1
            当dp[1][i-1]=0时，dp[1][i] = 0
        2) 当nums[i]<0时
            dp[1][i] = dp[0][i-1] + 1
            当dp[1][i-1]>0时，dp[0][i] = dp[1][i-1] + 1
            当dp[1][i-1]=0时，dp[0][i] = 0
        3) 当nums[i]=0时
            dp[0][i-1] = 0
            dp[1][i-1] = 0
        """
        n = len(nums)
        # 动态数组初始化
        dp = [[0] * n for _ in range(2)]
        res = 0
        if nums[0] > 0:
            dp[0][0] = 1
            res = 1
        elif nums[0] < 0:
            dp[1][0] = 1
        
        # 动态传递过程
        for i in range(1, n):
            if nums[i] > 0:
                dp[0][i] = dp[0][i-1] + 1
                if dp[1][i-1] > 0:
                    dp[1][i] = dp[1][i-1] + 1
                elif dp[1][i-1] == 0:
                    dp[1][i] = 0
            elif nums[i] < 0:
                dp[1][i] = dp[0][i-1] + 1
                if dp[1][i-1] > 0:
                    dp[0][i] = dp[1][i-1] + 1
                elif dp[1][i-1] == 0:
                    dp[0][i] = 0
            elif nums[i] == 0:
                dp[0][i] = 0
                dp[1][i] = 0
            res = max(res, dp[0][i])
        return res