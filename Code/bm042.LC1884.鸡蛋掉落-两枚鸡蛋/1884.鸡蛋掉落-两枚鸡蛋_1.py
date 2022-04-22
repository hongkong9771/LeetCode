class Solution:
    def twoEggDrop(self, n: int) -> int:
        """
        dp[i][j]表示还剩i+1个鸡蛋时，验证j个楼层所需要的最小操作次数
        1.当i = 0时，还剩1个鸡蛋，验证j个楼层所需要的最少操作次数为j次，即从第1层开始，一直验证到j层；
        2.当i = 1时，还剩2个鸡蛋，对于第1个鸡蛋，我们从1~j层楼中选第k层落下，共有两种情况：
          1）鸡蛋破碎，则接下来只需判断1~k-1层楼（共k-1层）即可，剩余操作次数为dp[0][k-1]，总的操作次数为1+dp[0][k-1]
          2）鸡蛋未破碎，则接下来只需判断k+1~j层楼（共j-k层）即可，剩余操作次数为dp[1][j-k]，总的操作次数为1+dp[1][j-k]
          取二者之间的最大值，即可求最小操作次数
        """
        # 动态数组初始化
        maxValue = float('inf')
        dp = [[maxValue] * (n+1) for _ in range(2)]
        dp[0][0], dp[1][0] = 0, 0
        for j in range(n+1):
            dp[0][j] = j
        
        # 动态传递过程
        for j in range(1, n+1):
            for k in range(1, j+1):
                dp[1][j] = min(dp[1][j], max(dp[0][k-1], dp[1][j-k])+1)
        return dp[1][n]