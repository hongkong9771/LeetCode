"""
题目描述:
对于任何正整数 m，是否存在非负整数 a 和 b，使得其满足 2^a+2^b=m,如满足，
则按照升序返回a,b，如不满足，则返回-1

"""

import math
M = int(input())


def zs(M):
    upper = math.log2(M)
    if M & (M-1) == 0:
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


res = zs(M)
ouput = " ".join(map(str, res))
print(ouput)
# print(res)