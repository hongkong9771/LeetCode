"""
题目描述:
对于任意一个字符串，可以对两个相邻位置的字符进行标记，但标记需满足以下条件: 两个字母是相同的，
或者两个字母是相邻的。并且，已经标记后的数据不能再进行标记，对字符标记的分数按照如下规则进行，
标记a加1分，标记b加2分，...标记z加26分
求能够获得的最高分？
样例1:
输入: abdbb
输出: 7

样例2:
输入: abb
输出: 4

思路: 
首先，对于动态数组dp[i]的定义为包含当前i个字符的最高分数
对于第i个字符，是否对其进行标记，首先取决于其是否可以被标记，分两种情况讨论:
1.可以被标记，则判断不对其进行标记的分数与对其进行标记的分数，取较大值
    a.不对其进行标记时，其分数与前一个字符的最大分数相同，即dp[i] = dp[i-1]
    b.对其进行标记时，其分数为dp[i-2]的分数与加上第i-1与i个字符的分数
2.不可以被标记，则包含当前i个字符的最高分数与dp[i-1]相同，即dp[i] = dp[i-1]
"""
inp = input()


def dynamic(inp):
    l = len(inp)
    if l == 1:
        return 0
    grade = [i for i in range(1, 27)]       # 计分数组
    dp = [0] * l
    # 初始化dp数组
    if abs(ord(inp[1]) - ord(inp[0])) < 2:
        dp[1] = grade[ord(inp[1])-97] + grade[ord(inp[0])-97]   # 97为字符'a'对应的ASCII码
    # 更新dp数组
    for i in range(2, l):
        # 如果满足标记条件，则判断不加入当前字符与加入当前字符后的分数，取较大值
        if abs(ord(inp[i]) - ord(inp[i-1])) < 2:
            dp[i] = max(dp[i-1], dp[i-2] + grade[ord(inp[i])-97] + grade[ord(inp[i-1])-97])
        else:
            dp[i] = dp[i-1]
    return dp[-1]


res = dynamic(inp)
print(res)