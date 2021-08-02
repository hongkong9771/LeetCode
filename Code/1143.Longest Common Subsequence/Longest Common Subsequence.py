class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp[i][j]表示包含text1[i]和text2[j]的两个字符串的最长公共子序列的长度
        当text1[i]=text2[j]时，dp[i][j]=dp[i-1][j-1]+1
        当text1[i]!=text2[j]时，dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        """

        l1 = len(text1)
        l2 = len(text2)
        # 初始化动态数组
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        res = 0
        # 动态传递
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1][l2]