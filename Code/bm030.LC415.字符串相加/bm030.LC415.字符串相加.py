class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
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