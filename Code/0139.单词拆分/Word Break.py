class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i]表示字符串长度为i的字符串s能否被拆分为一个或多个在字典中出现的单词，
        如果可以，则为true、反之为false
        dp[i]是否可以正确拆分，取决于s[i-k:i]在wordDict中，且dp[i-k]能正确拆分
        """
        l = len(s)
        dp = [False] * (l + 1)
        # 初始化动态数组
        dp[0] = True

        # 动态传递
        for i in range(1, l+1): # 先遍历背包，再遍历物品
            for word in wordDict:
                if len(word) <= i:
                    dp[i] = dp[i] or dp[i-len(word)] and word == s[i-len(word):i]
        return dp[-1]