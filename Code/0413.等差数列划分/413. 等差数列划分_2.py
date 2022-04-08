class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        对于一个长度为L的等差数列而言，如果后面接上一个数，得到一个长度为L+1的等差数列，
        则其对结果的贡献值可由之前长度为L的等差数列的贡献值得来。
        假设以nums[i]结尾的数的等差数组的子数组个数为dp[i]，一共有以下两种情况：
        1) 当nums[i]-nums[i-1] = nums[i-1]-nums[i-2]时，dp[i] = dp[i-1] + 1
        2) 当nums[i]-nums[i-1] != nums[i-1]-nums[i-2]时，dp[i] = 0
        因为每一个dp[i]均只与前一个状态有关，因此可采取压缩数组的方式进行。
        """

        n = len(nums)

        # 动态数组初始化
        dp = [0] * 2
        res = 0     # 记录所有的个数
        # 动态传递过程
        for i in range(2, n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i%2] = dp[(i-1)%2] + 1
            else:   
                dp[i%2] = 0   # 此行代码也可删除，写出来知识为了保证代码的可读性与完整性
            res += dp[i%2]
        return res