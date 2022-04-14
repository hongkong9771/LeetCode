class Solution:
    def addStrings(self, num1, num2):
        """
        对于两个非负整数的字符串，可以先比较其长度，然后在前面补0，
        对应位置相加，如果满10则进1，并将当前个位数放置在该位置
        """
        n1 = len(num1)
        n2 = len(num2)

        if n1 > n2:
            num2 = "0" * (n1-n2) + num2
        elif n1 < n2:
            num1 = "0" * (n2-n1) + num1
        Sum = 0
        carry = 0
        res = ""
        for i in range(max(n1, n2)-1, -1, -1):
            Sum = int(num1[i]) + int(num2[i]) + carry
            carry = 0       # 进位加上之后，需要将其置为0
            if Sum >= 10:   # 如果需要进位
                carry = 1
                Sum = Sum - 10
            res = str(Sum) + res
        if carry == 1:
            res = str(carry) + res
        return res

    def multiply(self, num1: str, num2: str) -> str:
        """
        将num2拆分成一个个的整数，然后分别与num1相乘，乘完后的结果进行两两相加，即为最终的结果。
        两两相加可以直接调用LC415的字符串相加
        """
        n1 = len(num1)
        n2 = len(num2)
        res = "0"       # 最终的结果
        for i in range(n1-1, -1, -1):
            if num1[i] == '0':
                continue
            tmp = ""     # 用于记录相乘后的中间结果
            carry = 0
            for j in range(n2-1, -1, -1):
                multi = int(num1[i]) * int(num2[j]) + carry
                carry = 0
                if multi >= 10:
                    carry = multi // 10     # 进位
                    multi = multi % 10      # 当前位
                tmp = str(multi) + tmp
            if carry != 0:
                tmp = str(carry) + tmp
            tmp = tmp + '0' * (n1-1-i)      # 乘10(单个的整数要考虑在个位、十位、百位、千位、、、)
            tmp = tmp.lstrip("0")           # 去除掉左边多余的0
            res = self.addStrings(res, tmp)
        return res





