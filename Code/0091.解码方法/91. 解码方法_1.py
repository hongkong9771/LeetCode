class Solution:
    def numDecodings(self, s: str) -> int:
        """
        对于数字字符串s，假设dp[i]表示以s[i]结尾的译码方法总数
        一共有以下几种情况：
        1.当s[i]='0'时：
            如果s[i-1]='1'或者s[i-1]='2'，则'0'和'1'或者'2'组合，则dp[i] = dp[i-2]
            如果s[i-1]!='1'或者'2'，则'0'无法与任何数字组合配对，直接返回0
        2.当s[i-1]='1'时：
            如果s[i-1]与s[i]组合译码，则共有dp[i-2]种方法
            如果s[i-1]与s[i]分开译码，则共有dp[i-1]种方法
            则dp[i] = dp[i-1] + dp[i-2]
        3.当s[i-1]='2'时：
            如果s[i]在1~6之间，则s[i-1]与s[i]可组合译码，也可分开译码，共有dp[i-1] + dp[i-2]种方法
            如果s[i]不在1~6之间，则s[i-1]与s[i]只能分开译码，共有dp[i-1]种方法
        4.当s[i-1]!='1'或者'2'时，则s[i-1]与s[i]只能分开译码，共有dp[i-1]种方法
        """
        n = len(s)

        # 动态数组初始化
        dp = [0] * n

        if s[0] == '0':
            return 0
        else:
            dp[-1] = 1  # 此处的dp[-1]并不代表最后一个的方法总数，而是便于当i-2小于0（越界）时进行计算
            dp[0] = 1
        
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] == '1':
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-1] == '2':
                if '1' <= s[i] <= '6':
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]