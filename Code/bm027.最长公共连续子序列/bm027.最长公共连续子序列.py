""""
    获取两个字符串中最大相同子串，比如str1 = "abcwerthelloyuiodef"; str2 = "cvhellobnm"
    提示：与 LeetCode.1143最长公共子序列类似，只不过这题要求公共子序列是连续的。
"""

"""
dp[i][j]表示包含str1[i]和str2[j]的最大相同子串的长度
当str1[i]和str2[j]相同时，dp[i][j] = dp[i-1][j-1]
当str1[i]和str2[j]不相同时，dp[i][j] = 0
"""


def find(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    dp = [[0] * (l2+1) for _ in range(l1+1)]
    res = 0
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            res = max(res, dp[i][j])
    return res


str1 = "abcwerthelloyuiodef"
str2 = "cvabcwe"

res = find(str1, str2)
print(res)
