class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        对于每一个字符串[i,j]，用dp[i][j]表示该范围内的字符串是否为回文串，若为回文串，则为True，反之则为False
        当s[i]!=s[j]时，则dp[i][j]必定为False
        当s[i]=s[j]时，可分为以下几种情况：
        1.当j=i时，此时只有一个字符，因此dp[i][j]=True
        2.当j-i=1时，此时有两个相等的字符，例如"aa"，因此dp[i][j]=True
        3.当j-i=2时，此时有三个字符，例如"aba"，因此dp[i][j]=True
        4.当j-i>2时，dp[i][j]是否为回文串，取决于内部的dp[i+1][j-1]是否为回文串
        """

        l = len(s)

        dp = [[False] * l for _ in range(l)]

        # 动态传递过程
        res = 0
        for i in range(l-1,-1,-1):
            for j in range(i, l):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                        res += 1
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                        res += 1
        return res