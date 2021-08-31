class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        想要找到只包含1的最大正方形的面积，则只需找到最大正方形的边长即可。
        假设二维矩阵的大小为m*n，则dp[i][j]表示以(i,j)为右下角的矩阵所包含的最大正方形的边长
        当matrix(i,j)=0时，包含matrix(i,j)的正方形的最大边长为0，
        当matrix(i,j)=1时，dp[i][j]的值取决于其左侧dp[i][j-1]，上侧dp[i-1][j]，左上侧dp[i-1][j-1]，并取其中的最小值
        dp[i][j]=min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        """
        if len(matrix) == 0 and len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        # 动态数组初始化
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                res = max(res, dp[i][j])
        return res**2