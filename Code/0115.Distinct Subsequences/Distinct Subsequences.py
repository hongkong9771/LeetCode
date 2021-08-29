class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        LC1143题解：
        dp[i][j]表示包含text1[i]和text2[j]的两个字符串的最长公共子序列的长度
        当text1[i]=text2[j]时，dp[i][j]=dp[i-1][j-1]+1
        当text1[i]!=text2[j]时，dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        此题与LC1143题目类似，
        dp[i][j]表示以s[i-1]结尾的子序列包含以t[j-1]结尾的子序列的个数
        当s[i-1]=t[j-1]时，可以使用s[i-1]来匹配，当然也可以不使用s[i-1]来匹配
        所以，dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
        当s[i-1]!=t[j-1]时，dp[i][j]=dp[i-1][j]

        关于初始化问题：
        dp[i][0]：表示对于任意空的字符串t，s字符串都可以通过删除所有字符变成空字符串
        dp[0][j]：表示对于任何空的字符串s，s字符串都无法变成t（除了t字符串为空的情况）
        因此dp[i][0]=1,dp[0][j]=0，其中dp[0][0]=1，空字符串s可以变为空字符串t
        """

        l1 = len(s)
        l2 = len(t)

        dp = [[0] * (l2+1) for _ in range(l1+1)]

        # 动态数组初始化
        for i in range(l1+1):
            dp[i][0] = 1
        for j in range(1,l2+1):
            dp[0][j] = 0
        
        # 动态传递
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[l1][l2]