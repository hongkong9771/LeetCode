class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        LC1143题解：
        dp[i][j]表示包含text1[i]和text2[j]的两个字符串的最长公共子序列的长度
        当text1[i]=text2[j]时，dp[i][j]=dp[i-1][j-1]+1
        当text1[i]!=text2[j]时，dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        此题与LC1143题目类似
        LC1143是判断两个字符串的公共子字符串的长度，而此题是要求字符串s是否为字符串t的子序列
        即只需判断最长公共子字符串的长度是否和s字符串的长度相等即可
        """

        l1 = len(s)
        l2 = len(t)
        # 动态数组初始化
        dp = [[0] * (l2+1) for _ in range(l1+1)]

        # 动态传递过程
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]           # 此处是与LC1143不同之处，因为字符串s为最小公共子字符串，不可以再回退了，否则肯定不满足最终的要求
        return dp[l1][l2] == l1