class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        dp[k][i][j]表示第0-i个字符串放入容量为m个0（zero_m)、n个1(one_n)中的字符串的最大数量
        dp[i][j]表示在上述三维数组的基础上去掉一维（字符串），因为每一层数组的更新只与上一层数组有关
        """
        l = len(strs)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for k in range(1, l+1):
            num_one = strs[k-1].count('1')
            num_zero = strs[k-1].count('0')
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if num_one <= j and num_zero <= i:
                        dp[i][j] = max(dp[i][j], dp[i-num_zero][j-num_one]+1)
                    else:#此处可以省略，加上是为了逻辑更加完整
                        dp[i][j] = dp[i][j]
        return dp[m][n]