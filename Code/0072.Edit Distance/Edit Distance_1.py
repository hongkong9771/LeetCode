class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j]表示以word1[i-1]结尾的字符串和以word2[j-1]结尾的字符串想要变得相同，所需要经过的最少的操作数
        对单词 A 删除一个字符和对单词 B 插入一个字符是等价的。例如当单词 A 为 doge，单词 B 为 dog 时，
        我们既可以删除单词 A 的最后一个字符 e，得到相同的 dog，也可以在单词 B 末尾添加一个字符 e，得到相同的 doge；

        这样以来，我们就可以把原问题转化为规模较小的子问题。我们用 A = horse，B = ros 作为例子，
        来看一看是如何把这个问题转化为规模较小的若干子问题的。

        在单词 A 中插入一个字符：如果我们知道 horse 到 ro 的编辑距离为 a，那么显然 horse 到 ros 的编辑距离不会超过 a + 1。
        这是因为我们可以在 a 次操作后将 horse 和 ro 变为相同的字符串，只需要额外的 1 次操作，在单词 A 的末尾添加字符 s，
        就能在 a + 1 次操作后将 horse 和 ro 变为相同的字符串；

        在单词 B 中插入一个字符：如果我们知道 hors 到 ros 的编辑距离为 b，那么显然 horse 到 ros 的编辑距离
        不会超过 b + 1，原因同上；

        修改单词 A 的一个字符：如果我们知道 hors 到 ro 的编辑距离为 c，那么显然 horse 到 ros 的编辑距离不会
        超过 c + 1，原因同上。

        dp[i][j-1]为 A 的前 i 个字符和 B 的前 j - 1 个字符编辑距离的子问题。即对于 B 的第 j 个字符，我们在 A 
        的末尾添加了一个相同的字符，那么 dp[i][j] 最小可以为 dp[i][j-1] + 1；
        dp[i-1][j] 为 A 的前 i - 1 个字符和 B 的前 j 个字符编辑距离的子问题。即对于 A 的第 i 个字符，我们在 B 
        的末尾添加了一个相同的字符，那么 dp[i][j] 最小可以为 dp[i-1][j] + 1；

        dp[i-1][j-1] 为 A 前 i - 1 个字符和 B 的前 j - 1 个字符编辑距离的子问题。即对于 B 的第 j 个字符，我们修改 A 
        的第 i 个字符使它们相同，那么 dp[i][j] 最小可以为 dp[i-1][j-1] + 1。
        特别地，如果 A 的第 i 个字符和 B 的第 j 个字符原本就相同，那么我们实际上不需要进行修改操作。在这种情况下，
        dp[i][j] 最小可以为 dp[i-1][j-1]。

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
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)

        return dp[l1][l2]