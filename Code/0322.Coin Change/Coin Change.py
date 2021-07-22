class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        此题也是完全背包
        dp[i]表示凑够总金额为amount的组合中的硬币数量最少的个数
        """
        # 对于每一个amount，所需的最少硬币个数为amount+1，所以这里取初始值为amoun+1
        l = len(coins)
        dp = [amount+1] * (amount + 1)

        # 初始化动态数组
        dp[0] = 0

        # 动态传递
        for i in range(1,amount+1):
            for j in range(l):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]