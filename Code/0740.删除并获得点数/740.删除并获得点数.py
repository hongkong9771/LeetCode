class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        此题与LC198.打家劫舍有点类似，连着的整数相当于连着的房屋，整数的点数乘以个数相当于房屋内的金额
        维护一个数组cnt,用于记录每个整数的个数，即cnt[i]表示整数i出现的次数。
        dp[i]表示到整数i时，所获得的最大点数。因此，一共有以下两种情况：
        1) 删除整数i时，dp[i]=dp[i-2]+cnt[i]*i
        2) 不删除整数i时，dp[i]=dp[i-1]
        """
        Max = max(nums)
        cnt = [0] * (Max+1)

        for i in nums:
            cnt[i] = cnt[i] + 1
        
        # 初始化动态数组dp
        dp = [0] * (Max+1)
        dp[1] = cnt[1] * 1
        
        for i in range(2, Max+1):
            dp[i] = max(dp[i-2]+cnt[i]*i, dp[i-1])
        return dp[-1]