class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp[i]表示爬到第i个台阶上的最小花费，最后一次爬楼有两种方式，从倒数第一阶往上爬1个台阶，
        从倒数第二阶往上爬2个台阶，那么最终要求的达到楼顶的最低花费即为min(dp[i-1]+cost[i-1], dp[-2]+cost[i-2])
        """
        # 初始化动态数组
        dp = [0, 0]

        # 动态传递过程
        for i in range(2, len(cost)):
            dp[0], dp[1] = dp[1], min(dp[0]+cost[i-2], dp[1]+cost[i-1])
        res = min(dp[0]+cost[-2], dp[1]+cost[-1])
        return res