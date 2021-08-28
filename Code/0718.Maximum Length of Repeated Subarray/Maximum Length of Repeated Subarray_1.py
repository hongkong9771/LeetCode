class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        dp[i][j]表示分别以A[i-1]、B[j-1]为结尾并包含A[i-1]、B[j-1]的公共子数组的长度，
        两层for循环分别遍历整数数组A和B，当A中的一个值与B中的值相等时，此时的dp[i][j]的值为：
        dp[i][j] = dp[i-1][j-1]+1
        """
        l_a = len(nums1)
        l_b = len(nums2)
        # 动态数组初始化
        dp = [[0] * (l_b+1) for _ in range(l_a+1)]
        # 动态传递
        res = 0
        for i in range(1, l_a+1):
            for j in range(1, l_b+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res =  max(res, dp[i][j])
        return res