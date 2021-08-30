class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        此题与LC647.回文子串有点区别，LC647题要求回文子串是连续的，而此处是不连续的
        因此，假设dp[i][j]表示s[i,j]范围内的字符串的最长回文子串
        当s[i]==s[j]时，dp[i][j]=dp[i+1][j-1]+2
        当s[i]!=s[j]时，可以选择i向右移一位，或者j向左移一位，则dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        注意：j是始终大于等于i的，这关系到i和j的遍历
        """

        l = len(s)

        dp = [[0] * l for _ in range(l)]

        # 动态数组初始化
        for i in range(l):
            dp[i][i] = 1
        
        # 动态传递
        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]