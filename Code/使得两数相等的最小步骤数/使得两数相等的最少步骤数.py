# encoding:utf-8
"""
@author: 危红康
@time: 2021/9/4 21:36
@file: 使两个整数相等的最少操作数.py
@software: Pycharm
"""


"""
有两个整数a, b，只能进行+1，-1，*2操作，使得两个数相等的最少操作步数
"""


# 情况一：只考虑两个数都为正整数
def operate1(a, b):
    """
    题目是求使得两个数相等的最少的操作步数，因此，小数往大数进行操作，步数会更快（因为有*2的步骤）
    假设b为其中较大的数
    dp[i]表示从整数a（二者中小一点的数）到i的最小操作步数
    """
    dp = [0] * (b+1)
    # 从a到小于a的数所需要的操作步数初始化
    for i in range(a-1, -1, -1):
        dp[i] = dp[i+1] + 1

    for i in range(a+1, b+1):
        if i % 2 == 0:      # i为偶数
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)      # 此处dp[i+1]无法计算，且经过推算，dp[i+1]到dp[i]会需要更多的操作步数，下面同理
        else:               # i为奇数
            dp[i] = min(dp[i-1]+1, dp[(i+1)//2]+2)
    return dp[b]


# 情况二：只考虑两个数都为负整数
"""
因为两个数都为负数和两个数都为正数的情况是一样的，将两个负数加绝对值之后再进行操作也是相同的结果
"""

# 情况三：一个为负数，一个为正数
"""
一个负数要想变成正数（刚好为0），只能通过+1操作，
同样的，一个正想要变成负数（刚好），也只能通过-1操作
所以操作步数为：从负数到0所需的操作步数+从0到正数所需的操作步数，即|a| + operate1(0,b)
"""


def operate_final(a, b):
    if a >= 0 and b >= 0:       # 情况一
        a = min(a, b)
        b = max(a, b)
        res = operate1(a, b)
    elif a < 0 and b < 0:       # 情况二
        a = abs(a)
        b = abs(b)
        a = min(a, b)
        b = max(a, b)
        res = operate1(a, b)
    elif a < 0 and b >= 0:      # 情况三
        res = operate1(0, b) + abs(a)
    elif a >= 0 and b < 0:
        res = operate1(0, a) + abs(b)
    return res


a = -2
b = 3
res = operate_final(a, b)
print(res)