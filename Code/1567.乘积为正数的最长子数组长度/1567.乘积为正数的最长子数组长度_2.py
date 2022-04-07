class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """
        1.未压缩数组形式
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
        
        2.压缩数组形式
        无论是正数还是负数，都只用到了两个相邻的状态，因此，可以采用压缩数组的形式来减小内存的使用。
        """
        n = len(nums)
        # 动态数组初始化
        positive, negative = 0, 0
        res = 0
        if nums[0] > 0:
            positive = 1
            res = 1
        elif nums[0] < 0:
            negative = 1
        
        # 动态传递过程
        for i in range(1, n):
            if nums[i] > 0:
                positive = positive + 1
                if negative > 0:
                    negative = negative + 1
                elif negative == 0:
                    negative = 0
            elif nums[i] < 0:
                New_negative = positive + 1     # 下面的判断用的还是原来的negative
                if negative > 0:
                    positive = negative + 1
                elif negative == 0:
                    positive = 0
                negative = New_negative
            elif nums[i] == 0:
                positive = 0
                negative = 0
            
            res = max(res, positive)
        return res