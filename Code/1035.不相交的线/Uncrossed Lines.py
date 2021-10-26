class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        """
        LC1143题解
        dp[i][j]表示包含text1[i]和text2[j]的两个字符串的最长公共子序列的长度
        当text1[i]=text2[j]时，dp[i][j]=dp[i-1][j-1]+1
        当text1[i]!=text2[j]时，dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        此题与LC1143最长公共子序列题是一样的，
        首先分析此题，要想找到不相交的最大连线数，则需满足nums[i]==nums[j]，且按顺序排列
        即为从nums1和nums2中找到公共子数组，且这个子数组的相对顺序不能改变，因此就和LC1143题一模一样了

        """

        l1 = len(nums1)
        l2 = len(nums2)

        dp = [[0] * (l2+1) for _ in range(l1+1)]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[l1][l2]