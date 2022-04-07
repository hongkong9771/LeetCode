class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        此题即从每层中找到最小的值作为路径，但是需要满足题目中所给出的条件（最多相隔一列），
        即符合条件的最小值。
        dp[i][j]表示走到i行j列时的最小路径和，其可以由其正上方的位置走过来，也可以从正上方
        左右两边的两个位置走过来，因此，只需取最小的那个位置即可。但是需要注意边界问题，即无左边位置
        或者无右边位置、或者即无左边位置也无右边位置（当n为1时）
        """
        n = len(matrix)

        # 动态数组初始化
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        # 动态传递过程
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j:j+2]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1:j+2]) + matrix[i][j]
        res = min(dp[n-1])
        return res