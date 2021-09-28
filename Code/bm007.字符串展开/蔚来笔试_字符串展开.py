# -*- coding:utf-8 -*- 
# @Time : 2021/9/25 19:29
# @Author : 危红康
# @File : 字符串展开.py
# @Software: PyCharm

"""
蔚来笔试题(2021.9.25)
有如下字符串："{a,b}c{d,e}"，它表示多个字符串的集合，其中括号{a,b}表示集合中的字符串可以任意取一个。
所以原字符串"{a,b}c{d,e}"可以展开成如下的四个字符串："acd", "bcd"，"ace"，"bce"。请你编写一段代码，
把包含括号的字符串展开成多个。
注：{}内的可以为字符串，不一定只是单个字符
"""
string = "zj{av,b}c{d,e}g"
# string = "abcd"
# string = "ax{bv,c,d}d"
# string = "a{b,c}{d,e}"
res = []
l = len(string)
i = 0

# while i < l:
#     if string[i] == "{":
#         temp = []
#         i += 1
#         while string[i] != "}":
#             if string[i] != ",":
#                 temp.append(string[i])
#             i += 1
#         res.append(temp)
#     elif string[i] == "}":
#         i += 1
#     else:
#         temp = []
#         temp.append(string[i])
#         i += 1
#         res.append(temp)

while i < l:
    if string[i] == "{":
        ss = ""                 # 统计字符串
        temp = []
        i += 1
        while string[i] != "}":
            if string[i] != ",":
                ss += string[i]
            else:
                temp.append(ss)
                ss = ""
            i += 1
        temp.append(ss)
        res.append(temp)
    elif string[i] == "}":
        i += 1
    else:
        ss = ""                 # 统计字符串
        temp = []
        while i < l and string[i] != "{":
            ss += string[i]
            i += 1
        temp.append(ss)
        res.append(temp)

res = [x for x in res if x != []]


print(res)
result = []
path = []


def dfs(res, index):
    if index == len(res):
        result.append(path[:])
        return

    for i in range(len(res[index])):
        path.append(res[index][i])
        dfs(res, index+1)
        path.pop()


dfs(res, 0)
final_result = []
for i in range(len(result)):
    ss = "".join(result[i])
    final_result.append(ss)


print(final_result)

