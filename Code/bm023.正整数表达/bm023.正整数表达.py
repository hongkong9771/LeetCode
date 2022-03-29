# -*- coding:utf-8 -*- 
# @Time : 2022/3/17 18:03
# @Author : 危红康
# @File : 正整数表达.py
# @Software: PyCharm


"""
题目描述:
对于任何正整数 m，是否存在非负整数 a 和 b，使得其满足 2^a+2^b=m,如满足，
则按照升序返回a,b，如不满足，则返回-1

"""

import math
M = int(input())

"""
# 这种方法时间复杂度有问题。
def zs(M):
    upper = math.log2(M)
    if M & (M-1) == 0:      # 判断是否为2的幂次方
        upper = int(upper)
    else:
        upper = int(upper) + 1
    for a in range(upper):
        for b in range(a, upper):
            if 2 ** a + 2 ** b == M:
                return [a, b]
            elif 2 ** a + 2 ** b > M:
                return [-1]
            if a == upper - 1 and b == upper - 1:
                return [-1]
    return [-1]
"""

"""
将整数M用二进制"01"表示，当该整数的二进制包含1个或者2个'1'时，说明其可由其它2的指数次幂组成，
当只包含1个'1'时，以4('0100')为例，则由位于4后面的两个1组成，即'0010'和'0010'，也就是2^1+2^1。
当包含2个'1'时，以6('0110')为例，则由位于第1和第2个位置处（从右往左数）的两个'1'组成，即'0010'
和'0100'，也就是2^1+2^2
"""


def zs(M):
    if M == 1:
        return [-1]
    res = bin(M).replace("0b", "")
    # print(res)
    l = len(res)
    num_1 = res.count('1')
    if num_1 > 2:
        return [-1]
    elif num_1 == 1:
        ind = res.index('1')
        a, b = l - ind - 2, l - ind - 2
        return [a, b]
    elif num_1 == 2:
        ind1 = res.index('1')
        b = l - ind1 - 1
        ind2 = res[ind1+1:].index('1') + ind1 + 1
        a = l - ind2 - 1
        return [a, b]


res = zs(M)
ouput = " ".join(map(str, res))
print(ouput)