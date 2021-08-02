class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        dp[i][j]表示分别以A[i]、B[j]为结尾并包含A[i]、B[j]的公共子数组的长度，
        两层for循环分别遍历整数数组A和B，当A中的一个值与B中的值相等时，此时的dp[i][j]的值为：
        dp[i][j] = dp[i-1][j-1]+1
        因为每一个状态都只与前一个状态有关，所以，可以采用压缩数组的方法实现
        """
        l_a = len(nums1)
        l_b = len(nums2)
        # 动态数组初始化
        dp = [0] * (l_b+1)
        # 动态传递
        res = 0
        for i in range(1, l_a+1):
            for j in range(l_b, 0, -1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1] + 1
                else:
                    dp[j] = 0       # 不相等的时候需要进行赋0操作，否则。会继承之前的值
                res =  max(res, dp[j])
        return res