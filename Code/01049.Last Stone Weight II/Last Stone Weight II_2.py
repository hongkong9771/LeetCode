class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        题目的思想就是在stones列表中找到几个元素，使得其和接近sum(stones)/2，
        这样才能满足最后的石头重量最小，当找到的元素和刚好等于sum的一半时，最后没有石头。
        """
        l = len(stones)
        S = sum(stones)//2      # 向下取整，当sum(stones)
        # 当stones中存在一个数大于S（stones和的一半）时，最后石头的最小重量如下:
        if max(stones) > S:
            return 2*max(stones) - sum(stones)
        # dp数组初始化
        # dp = [[0]*(S+1) for _ in range(l)]
        dp = [0]*(S+1)
        for k in range(stones[0], S+1):
            dp[k] = stones[0]
        
        # 动态传递过程
        for i in range(1, l):
            for j in range(S, 0, -1):
            # for j in range(1, S+1):
                if stones[i] <= j:
                    dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
                else:
                    dp[j] = dp[j]
        return sum(stones)-dp[S]*2
