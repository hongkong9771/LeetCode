class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        此题与LC647.回文子串类似，
        *****************************LC647题的题解*********************************
        对于每一个字符串[i,j]，用dp[i][j]表示该范围内的字符串是否为回文串，若为回文串，则为True，反之则为False
        当s[i]!=s[j]时，则dp[i][j]必定为False
        当s[i]=s[j]时，可分为以下几种情况：
        1.当j=i时，此时只有一个字符，因此dp[i][j]=True
        2.当j-i=1时，此时有两个相等的字符，例如"aa"，因此dp[i][j]=True
        3.当j-i=2时，此时有三个字符，例如"aba"，因此dp[i][j]=True
        4.当j-i>2时，dp[i][j]是否为回文串，取决于内部的dp[i+1][j-1]是否为回文串

        因此，只要判断dp[i][j]为True，就记录该回文子串的长度以及起始位置i，下一个回文子串的长度若大于该长度，则替换掉该次记录，
        成为新的最长回文子串
        """

        l = len(s)

        dp = [[False] * l for _ in range(l)]
        # 用于记录最长回文子串的长度和起始位置
        max_len = 0
        index = 0
        for i in range(l-1, -1, -1):
            for j in range(i, l):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                if dp[i][j] == True and j - i + 1 > max_len:
                    max_len = j - i + 1
                    index = i
        return s[index:index+max_len]