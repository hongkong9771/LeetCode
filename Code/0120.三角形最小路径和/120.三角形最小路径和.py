class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        此题与LC931.下降路径最小和类似，只不过这里从上面取得点的位置有些变化
        """
        n = len(triangle)   # 记录一共有多少行，对应第i行有i个数据
        # 初始化动态数组
        dp = [[0] * i for i in range(1, n+1)]
        dp[0][0] = triangle[0][0]

        # 动态传递过程
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j:j+1]) + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1:j+1]) + triangle[i][j]
        return min(dp[n-1])