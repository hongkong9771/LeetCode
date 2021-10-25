class Solution:
    def climbStairs(self, n: int) -> int:
        """
        此题可以理解成完全背包：
        每次爬的1个或2个台阶可以看成是物品的总类，共n阶楼梯可以看成是背包的总容量。
        因为每次都可以选择爬1阶或2阶楼梯，此外，1个或2个台阶是可以重复使用的，因此是完全背包
        """
        nums = [1, 2]
        dp = [0] * (n + 1)

        # 初始化动态数组
        dp[0] = 1

        # 动态传递
        for j in range(1,n+1):
            for i in range(2):
                if nums[i] <= j:
                    dp[j] = dp[j] + dp[j - nums[i]]
                else:   #此块代码可以省略，加上只是为了保证代码的完整性
                    dp[j] = dp[j]
        return dp[n]