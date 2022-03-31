class Solution:
    def numTrees(self, n: int) -> int:
        """
        dp[i]表示i个节点的二叉搜索树的种数
        当节点数量为n时，二叉搜索树的种数由左右子树的种数决定，
        当n=3时，共有以下几种情况：
        1) 当左、右子树分别为0、2个节点时，此时一共有dp[0]*dp[2]种
        2) 当左、右子树分别为1、1个节点时，此时一共有dp[1]*dp[1]种
        3) 当左、右子树分别为2、0个节点时，此时一共有dp[2]*dp[0]种
        以此计算最终的dp[n]
        """
        # 动态数组初始化
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] = dp[i] + dp[j]*dp[i-1-j]
        return dp[n]