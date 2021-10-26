class Solution:
    def numSquares(self, n: int) -> int:
        """
        完全背包+组合
        """
        # 动态数组初始化
        dp = [i for i in range(n+1)]

        # 动态传递
        for i in range(1,n):    # 先遍历物品
            if i**2 > n:
                break
            for j in range(i**2,n+1):   # 再遍历背包
                dp[j] = min(dp[j], dp[j-i**2]+1)
        return dp[-1]
        