class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        dp[k][i][j]表示第0-k个字符串放入容量为m个0（zero_m)、n个1(one_n)中的字符串的最大数量
        
        """
        l = len(strs)
        dp = [[[0]*(n+1) for i in range(m+1)] for j in range(l+1)]
        for k in range(1,l+1):
            num_one = strs[k-1].count('1')
            num_zero = strs[k-1].count('0')
            for i in range(m+1):
                for j in range(n+1):
                    if num_one <= j and num_zero <= i:
                        dp[k][i][j] = max(dp[k-1][i][j], dp[k-1][i-num_zero][j-num_one]+1)
                    else:
                        dp[k][i][j] = dp[k-1][i][j]
        return dp[l][m][n]