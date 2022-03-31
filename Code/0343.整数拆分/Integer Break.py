class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * ( n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                # 假设对正整数 i 拆分出的第一个正整数是 j（1 <= j < i），则有以下两种方案：
                # 1) 将 i 拆分成 j 和 i−j 的和，且 i−j 不再拆分成多个正整数，此时的乘积是 j * (i-j)
                # 2) 将 i 拆分成 j 和 i−j 的和，且 i−j 继续拆分成多个正整数，此时的乘积是 j * dp[i-j]
                dp[i] = max(dp[i], max(j*(i-j), j * dp[i-j]))
        return dp[-1]