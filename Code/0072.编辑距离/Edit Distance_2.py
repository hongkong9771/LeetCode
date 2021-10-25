class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j]表示以word1[i-1]结尾的字符串和以word2[j-1]结尾的字符串想要变得相同，所需要经过的最少的操作数
        当word1[i-1]=word2[j-1]，不需要进行任何操作，所以dp[i][j]=dp[i-1][j-1]
        当word1[i-1]!=word2[j-1]
        操作一：word1增加一个元素，使其word1[i - 1]与word2[j - 1]相同，那么就是以下标i-2为结尾的word1 与 j-1为结尾的word2的
        最近 编辑距离 加上一个增加元素的操作。即 dp[i][j] = dp[i - 1][j] + 1;

        操作二：word2添加一个元素，使其word1[i - 1]与word2[j - 1]相同，那么就是以下标i-1为结尾的word1 与 j-2为结尾的word2的
        最近编辑距离 加上一个增加元素的操作。即 dp[i][j] = dp[i][j - 1] + 1;

        操作三：替换元素，word1替换word1[i - 1]，使其与word2[j - 1]相同，此时不用增加元素，那么以下标i-2为结尾的word1 与 j-2
        为结尾的word2的最近编辑距离 加上一个替换元素的操作。即 dp[i][j] = dp[i - 1][j - 1] + 1;
        """

        l1 = len(word1)
        l2 = len(word2)

        dp = [[0] * (l2+1) for _ in range(l1+1)]
        # 动态数组初始化
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j
        # 动态传递
        for i in range(1, l1+1):
            for j in range(1,l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)

        return dp[l1][l2]