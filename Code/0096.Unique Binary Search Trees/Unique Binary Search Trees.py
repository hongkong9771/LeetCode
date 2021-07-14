class Solution:
    def numTrees(self, n: int) -> int:
        # 初始化动态数组
        dp = [0] * (n + 1)
        dp[0] = 1

        # 给动态数组赋值
        for i in range(1, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[-1]