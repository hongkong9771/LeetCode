class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        假设带"+"的整数之和为pos，带"-"的整数之和则为sum(nums)-pos，则按照题意，需要满足以下条件：
        pos - (sum(nums) - pos) = 2*pos - sum(nums) = target,即pos = (sum(nums) + target)/2
        整个题目就变成了，从nums中选出一些数，使得其和为(sum(nums) + target)/2
        """
        s = sum(nums)
        l = len(nums)
        # pos为正整数，则sum(nums) + target为正偶整数
        if s < target or (s + target) % 2 == 1:
            return 0
        target_new = (s + target)//2

        # 初始化动态数组
        dp = [0] * (target_new + 1)
        dp[0] = 1
        
        # 动态传递过程
        for i in range(l):  # 此处从0——(l-1)感觉有点问题
            for j in range(target_new, -1, -1):     #j取到0是因为nums可能包含0
                if nums[i] <= j:
                    dp[j] = dp[j] + dp[j-nums[i]]
                else:
                    dp[j] = dp[j]
        return dp[target_new]