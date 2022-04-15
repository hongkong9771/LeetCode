# -*- coding:utf-8 -*- 
# @Time : 2022/4/14 19:10
# @Author : 危红康
# @File : 携程_游戏是9的倍数.py
# @Software: PyCharm


"""
对于一个数字串，求该数字串的所有子序列为9的倍数的个数。
其中，子序列可以包含前导0，若两个子序列在原串中的位置不同，则认为它们不同

输入描述：字符串的长度n<200000，仅由'0'~'9'十种字符组成
输入：1188
输出：5
解释：18 18 18 18 1188（一共5个）

输入：0123
输出：1
解释：0（一共1个）

"""


num_str = input()
k = int(input())
n = len(num_str)

"""
思路：首先有这样一条规律：所有为9的倍数的非负整数，其各个位之和也为9的倍数（可以互相推出）
因此，本题可以将数字字符串转换为数字数组，然后取子序列位置相加，若子序列相加之和为9的倍数，
则子序列组成的整数也应为9的倍数。（将9变成3也是成立的，证明的话，后面可以搜一下。）

然后使用动态规划（背包）的思想来做：
dp[i][j]表示前i个长度的所有子序列数之和对3取模为j的数目(0<=j<k，在此题中k为9)
因此，dp[i][j]共有如下两种情况：
1) 第i个数字不取，则dp[i][j] = dp[i-1][j]
2) 第i个数字取，则dp[i][j] = dp[i-1][(j-num[i]+k)%k]
最后这个数字自己构成长度为1的子序列单独加上
此为未压缩数组的方式，空间复杂度为O(n*k)，时间复杂度也为O(n*k)，通过观察可以发现，
每一次动态更新的过程中，都只与前一次的状态有关，因此，可采取压缩数组的方式进行。

"""


def generatePermutation(s, k):
    """
    # 未压缩数组的方式，空间复杂度为O(n*k)，时间复杂度也为O(n*k)
    mod = 10**9 + 7
    num = []
    for ss in s:
        num.append(int(ss))

    # 动态数组初始化
    dp = [[0] * k for _ in range(n)]
    dp[0][num[0] % k] = 1

    # 动态传递过程
    for i in range(1, n):
        # 每一个数对k取余，当k为9的情况下，可以省略此行代码，当k为3时，执行此行代码
        # （也可以在构造数组时，就进行取余操作）
        m = (num[i]) % k
        for j in range(k):
            dp[i][j] = (dp[i-1][j] + dp[i-1][(k+j-m) % k]) % mod
        dp[i][m] = (dp[i][m] + 1) % mod
    return dp[n-1][0] % mod
    """

    # 压缩数组的方式，空间复杂度为O(2*k)，时间复杂度为O(n*k)
    mod = 10 ** 9 + 7
    num = [int(ss) for ss in s]

    # 动态数组初始化
    dp = [[0] * k for _ in range(2)]
    dp[0][num[0] % k] = 1
    for i in range(1, n):
        m = (num[i]) % k
        for j in range(k):
            dp[i % 2][j] = (dp[(i-1) % 2][j] + dp[(i-1) % 2][(j - num[i] + k) % k]) % mod
        dp[i % 2][m] = (dp[i % 2][m] + 1) % mod
    return dp[(n-1) % 2][0]


cnt = generatePermutation(num_str, k)
print(cnt)




"""*************************** 回溯 *********************************"""
"""
思路：将所有子序列全部排列出来，并判断其是否为9的倍数
"""
"""
方法一：当数字字符串的长度较大时，会导致栈溢出
def subSequence(num_str, i, res, cnt):
    if i == len(num_str):
        if res != "" and int(res) % 9 == 0:
            cnt += 1
    else:
        cnt = subSequence(num_str, i+1, res, cnt)
        cnt = subSequence(num_str, i+1, res+num_str[i], cnt)
    return cnt % (10**9 + 7)


# cnt = subSequence(num_str, 0, "", 0)
# print(cnt)
"""

"""
方法二：当数字字符串的长度较大时，会导致栈溢出
def generatePermutation(s):
    cnt = 0

    def dfs(idx, t):
        nonlocal cnt
        if idx > len(s):
            return
        if t != "" and int(t) % 9 == 0:
            cnt += 1
        for i in range(idx, len(s)):
            dfs(i + 1, t + s[i])
    dfs(0, "")
    return cnt % (10**9 + 7)


# cnt = generatePermutation(num_str)
# print(cnt)
"""


"""*************************** 位运算 *********************************"""
"""
方法三：当数字字符串的长度较大时，会超时
def generatePermutation_2(s):
    cnt = 0
    for m in range((1 << n)):
        sb = ""
        for i in range(n):
            if m & (1 << i) != 0:
                sb += s[i]
        if len(sb) != 0 and int(sb) % 9 == 0:
            cnt += 1
    return cnt % (10**9 + 7)


# cnt = generatePermutation_2(num_str)
# print(cnt)
"""