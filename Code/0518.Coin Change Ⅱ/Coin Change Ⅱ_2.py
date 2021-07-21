class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp[i]表示装满总金额为i的背包的组合数
        """
        l = len(coins)
        
        dp = [0] * (amount + 1)

        # 初始化动态数组
        dp[0] = 1

        # 动态传递
        for i in range(l):
            for j in range(1,amount+1):
                if coins[i] <= j:
                    dp[j] = dp[j] + dp[j-coins[i]]
                else:   #此块代码可以省略，加上来是为了增强代码的可读性
                    dp[j] = dp[j]
        return dp[amount]
