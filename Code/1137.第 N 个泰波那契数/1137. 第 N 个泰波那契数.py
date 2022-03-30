class Solution:
    def tribonacci(self, n: int) -> int:
        """
        此题与LC509.斐波那契数类似
        此题是前三个数相加
        """
        # 特殊情况
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        
        # 直接使用压缩空间版的做法
        # 初始化动态矩阵dp
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp[0], dp[1], dp[2] = dp[1], dp[2], dp[0] + dp[1] + dp[2]
        return dp[-1]