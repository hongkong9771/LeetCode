class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp[i][j]表示前i个面额的硬币装满总金额为j的背包的组合数
        """
        l = len(coins)
        
        dp = [[0] * (amount+1) for _ in range(l)]

        # 初始化动态数组
        for i in range(l):
            dp[i][0] = 1
        
        if coins[0] <= amount:
            for j in range(coins[0], amount+1):
                dp[0][j] = dp[0][j] + dp[0][j-coins[0]]
        
        # 动态传递过程
        for i in range(1,l):
            for j in range(1,amount+1):
                if coins[i] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else: 
                    dp[i][j] = dp[i-1][j]
        return dp[l-1][amount]
        