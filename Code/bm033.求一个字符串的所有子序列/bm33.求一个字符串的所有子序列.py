# -*- coding:utf-8 -*- 
# @Time : 2022/4/15 16:05
# @Author : 危红康
# @File : 求一个字符串的所有子序列.py
# @Software: PyCharm


"""
题目描述：
求一个字符串的所有子序列，包含空字符串和重复的字符串（不重复的字符串则用set存储）

"""
string = input()


def subSequence(string):

    def dfs(num_str, i, res, cnt):
        if i == len(num_str):
            cnt += 1
            ans.append(res)
        else:
            cnt = dfs(num_str, i+1, res, cnt)
            cnt = dfs(num_str, i+1, res+num_str[i], cnt)
        return cnt % (10**9 + 7)
    ans = []
    cnt = dfs(string, 0, "", 0)
    return ans, cnt


"""
def subSequence(string):
    # 将cnt作为非局部变量使用，无需每次dfs都返回cnt
    def dfs(num_str, i, res):
        nonlocal cnt
        if i == len(num_str):
            cnt += 1
            ans.append(res)
        else:
            dfs(num_str, i+1, res)
            dfs(num_str, i+1, res+num_str[i])
        return cnt % (10**9 + 7)
    ans = []
    cnt = 0
    dfs(string, 0, "")
    return ans, cnt
"""

ans, cnt = subSequence(string)
print(ans, '\n', cnt)
