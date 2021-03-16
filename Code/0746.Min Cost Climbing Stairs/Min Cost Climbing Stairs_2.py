class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[0], cost[1]]
        for i in range(2, n):
            dp[0], dp[1] = dp[1], min(dp[0], dp[1]) + cost[i]
        return min(dp[0], dp[1])