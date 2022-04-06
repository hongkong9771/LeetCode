class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        1.未压缩数组：
        dp[i][j]表示走到第i行j列时的最小路径和，由于每次只能向下或者向右移动一步，则dp[i][j]可以表示为：
        1) 当往下移动至dp[i][j]时，dp[i][j] = dp[i-1][j]+grid[i][j]
        2) 当往右移动至dp[i][j]时，dp[i][j] = dp[i][j-1]+grid[i][j]
        取二者中的最小值即可
        即dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        2.压缩数组：
        dp[i] = min(dp[i], dp[i-1]) + grid[i][j]
        """
        #  行为m，列为n
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n
        # 初始化动态数组dp
        dp[0] = grid[0][0]
        # for i in range(1, m):
        #     dp[i] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        # 动态传递过程
        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[n-1]