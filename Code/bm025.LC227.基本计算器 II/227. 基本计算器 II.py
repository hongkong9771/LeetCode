class Solution:
    def calculate(self, s: str) -> int:
        # 用于存储所有已经计算好'*'和'/'后的结果，剩下的只需要相加就行了
        stack = []
        # operate表示碰到运算符时的前一个运算符，初始化为'+'，res表示中间的数字
        operate, res = '+', 0
        l = len(s)
        for i in range(l):
            if s[i].isdigit():
                res = 10 * res + int(s[i])
            if s[i] in "+-*/" or i == l - 1:
                if operate == '+':
                    stack.append(res)
                elif operate == '-':
                    stack.append(-res)
                elif operate == '*':
                    stack.append(stack.pop() * res)
                elif operate == '/':
                    tmp = stack.pop()
                    # 负数整除的情况
                    if tmp < 0:
                        stack.append(- ((-tmp) // res) )
                    else:
                        stack.append(tmp // res)
                res = 0
                operate = s[i]
        return sum(stack)